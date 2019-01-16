#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ftp.common.Exception import CmdException
from ftp.common.Message import Message
from ftp.common.Tools import MsgTool, ProgressTool, MD5Tool
from ftp.client.Config import ClientConfig
import os, socket


class ClientHandler:

    @staticmethod
    def handler(client, cmd_str):
        cmds = cmd_str.split()
        cmd_type = cmds[0]
        # 处理put命令
        if cmd_type == 'put':
            filename = cmds[1]
            ClientHandler.__put(client, ClientConfig.LOCAL_DIR, filename)
            return
        # 打印错误信息
        msg_dic = MsgTool.recvmsg(client)
        if "error" in msg_dic.keys():
            print(msg_dic['error'])
            return
        # 处理其他命令
        if cmd_type == 'get':
            ClientHandler.__get(client, msg_dic)
        elif cmd_type == 'ls':
            ClientHandler.__ls(msg_dic)
        elif cmd_type == 'del':
            ClientHandler.__del()
        elif cmd_type == 'mkdir':
            ClientHandler.__mkdir()
        elif cmd_type == 'cd':
            pass
        return msg_dic

    @staticmethod
    def __get(client, header_dic):
        total_size = header_dic['filesize']
        filename = header_dic['filename']
        file_path = os.path.join(ClientConfig.LOCAL_DIR, filename)
        is_exists = False
        choose = 'y'
        if os.path.isfile(file_path):
            is_exists = True
            choose = input('文件已存在,是否覆盖? y/n: ').strip()
        # 接收数据
        if not is_exists or (choose == 'y' and is_exists):
            bar = ProgressTool.progressbar(total_size)
            bar.__next__()
            with open(file_path, 'wb') as f:
                recv_size = 0
                while recv_size < total_size:
                    line = client.recv(1024)
                    recv_size += len(line)
                    if choose == 'y':
                        bar.send(recv_size)
                        f.write(line)
                print("")
        else:
            recv_size = 0
            while recv_size < total_size:
                line = client.recv(1024)
                recv_size += len(line)

    @staticmethod
    def __put(client: socket, localdir:str, filename: str):
        """
        下载文件
        :param ftpuser:
        :param conn:
        :param filename:
        :return:
        """
        file_path = os.path.join(localdir, filename)
        if not os.path.exists(file_path):
            raise CmdException("$文件不存在")
        # md5 = hashlib.md5()
        # md5.update()
        filesize = os.path.getsize(file_path)
        md5 = MD5Tool.getfilemd5(file_path)
        header_length, header_bytes = Message.file_header('put', filename, md5, filesize)
        # 报头长度
        client.send(header_length)
        # 报头
        client.send(header_bytes)
        #接收反馈
        msg_dic = MsgTool.recvmsg(client)
        if "error" in msg_dic.keys():
            print(msg_dic['error'])
            return
        # 发送文件数据
        bar = ProgressTool.progressbar(filesize)
        bar.__next__()
        rev_size = 0
        with open(file_path, 'rb') as f:
            for line in f:
                client.send(line)
                rev_size += len(line)
                bar.send(rev_size)
            f.close()
        print("")
        return True

    @staticmethod
    def __ls(header_dic):
        resp = header_dic['resp']
        for index, item in enumerate(resp):
            print(item, " ", end="")
            if (index+1) % 6 == 0:
                print("")
        print("")

    @staticmethod
    def __del():
        print("删除成功")

    @staticmethod
    def __mkdir():
        print("创建成功")


