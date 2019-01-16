#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, os
from ftp.server.CmdHandler import CmdHandler
from ftp.server.auth.AuthManage import AuthManage
from ftp.common.Message import Message
from ftp.common.Exception import CmdException
from ftp.server.config.Settings import ServerSettings


class FtpServer:

    def __init__(self):
        if not os.path.isdir(ServerSettings.FTP_SERVER_BASE_DIR_PATH): os.mkdir(ServerSettings.FTP_SERVER_BASE_DIR_PATH)

    def main(self, host, port):
        socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_server.bind((host, port))
        socket_server.listen(10)
        # 用户登录管理
        authmanage = AuthManage()
        while True:
            conn, addr = socket_server.accept()
            try:
                with conn:
                    print("client connected:", addr)
                    while True:
                        try:
                            try:
                                res = conn.recv(8096)
                            except ConnectionResetError:
                                print("client[{}]连接已断开".format(addr))
                                break;
                            except Exception:
                                break;
                            if not res: continue
                            try:
                                print(res)
                                CmdHandler.handler(conn, res.strip(), authmanage)
                            except CmdException as e:
                                raise CmdException(e.message)
                            except Exception as e:
                                raise CmdException("$非法命令")
                        except Exception as e:
                            if conn:
                                header_length, header_bytes = Message.error_resp_header(e.args[0])
                                # 报头长度
                                conn.send(header_length)
                                conn.send(header_bytes)
                            else:
                                break
            except Exception:
                print("client[{}]连接已断开".format(addr))
                continue


host = "127.0.0.1"
port = 2280
ftpserver = FtpServer()
ftpserver.main(host, port)
