#!/usr/bin/env python
# -*- coding: utf-8 -*-

import struct, json, hashlib, os
from ftp.common.Exception import CmdException


class MsgTool:

    @staticmethod
    def recvmsg(client):
        # 报头长度
        obj = client.recv(4)
        if not obj: raise CmdException("$报文为空")
        header_size = struct.unpack('i', obj)[0]
        # 报头
        header_bytes = client.recv(header_size)
        # 解析报头
        header_dic = json.loads(header_bytes.decode('utf-8'))
        return header_dic


class MD5Tool:

    @staticmethod
    def getfilemd5(filename):
        if not os.path.isfile(filename):
            return
        myhash = hashlib.md5()
        f = open(filename, 'rb')
        while True:
            b = f.read(8096)
            if not b:
                break
            myhash.update(b)
        f.close()
        return myhash.hexdigest()


class ProgressTool:

    @staticmethod
    def progressbar(total_size):
        final_percent = 0
        while True:
            recv_size = yield
            curr_percent = int(recv_size / total_size * 100)
            if curr_percent > final_percent or curr_percent == 100:
                print("#"*int(curr_percent / 2) + "{}%".format(curr_percent), end="\r", flush=True)
                final_percent = curr_percent


# print(MD5Tool.getfilemd5('D:/ftpclient/a'))