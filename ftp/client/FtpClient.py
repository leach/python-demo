#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, os

from ftp.client.ClientHandler import ClientHandler
from ftp.common.Message import Message
from ftp.common.Tools import MsgTool
from ftp.client.Config import ClientConfig


class FtpClient:
    def __init__(self):
        if not os.path.isdir(ClientConfig.LOCAL_DIR): os.mkdir(ClientConfig.LOCAL_DIR)

    def login(self, client):
        # 认证登录三次
        cnt = 0
        while cnt < 3:
            cnt += 1
            username = input("username:").strip()
            password = input("password:").strip()
            req_msg = Message.login_req_msg(username, password)
            client.send(req_msg)
            # 接收
            header_dic = MsgTool.recvmsg(client)
            if not header_dic or not 'auth' in header_dic.keys():
                print("$账户或密码错误")
                continue
            else:
                homedir = header_dic['homedir']
                currdir = header_dic['currdir']
                print("#登录成功, 根目录:{}, 当前目录:{}".format(homedir, currdir))
                return header_dic['auth'], currdir

    def main(self, host, port):
        """
        客户端
        :param host:
        :param port:
        :return:
        """
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        # 登录
        auth, currdir = self.login(client)
        if not auth:
            client.close()
            print("$登录失败")
            return
        # 执行命令
        while True:
            try:
                cmd = input("{}>>".format(currdir)).strip()
                if not cmd: continue
                if cmd == 'close':
                    print("$用户退出")
                    client.close()
                    break
                client.send(Message.cmd_req_msg(auth, cmd))
                # 处理返回报文
                msg_dic = ClientHandler.handler(client, cmd)
                if msg_dic and 'currdir' in msg_dic.keys(): currdir = msg_dic['currdir']
            except Exception as e:
                while True:
                    res = client.recv(1024)
                    if not res: break
                print("$命令异常")
                continue


host = "127.0.0.1"
port = 2280
ftpclient = FtpClient()
ftpclient.main(host, port)
