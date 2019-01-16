#!/usr/bin/env python
# -*- coding: utf-8 -*-

import struct, json


class Message:

    @staticmethod
    def cmd_req_msg(auth: str, cmd: str):
        """
        请求命令报文
        :param auth:
        :param cmd:
        :return:
        """
        cmd_msg = {
            "auth": auth,
            "cmd": cmd
        }
        return json.dumps(cmd_msg).encode("utf-8")

    @staticmethod
    def login_req_msg(username, password):
        """
        登录请求报文
        :param username:
        :param password:
        :return:
        """
        msg_dic = {
            "username": username,
            "password": password
        }
        return json.dumps(msg_dic).encode("utf-8")

    @staticmethod
    def login_success_msg(auth: str, homedir: str, currdir: str):
        """
        登录成功报文
        :param auth:
        :return:
        """
        header_dic = {
            "auth": auth,
            "homedir": homedir,
            "currdir": currdir
        }
        header_bytes = json.dumps(header_dic).encode("utf-8")
        header_length = struct.pack('i', len(header_bytes))
        return header_length, header_bytes

    @staticmethod
    def error_resp_header(error: str):
        """
        错误信息报文头
        :param error:
        :return:
        """
        header_dic = {
            'error': error
        }
        header_bytes = json.dumps(header_dic).encode('utf-8')
        header_length = struct.pack('i', len(header_bytes))
        return header_length, header_bytes

    @staticmethod
    def succ_resp_header(cmd_type, resp, currdir):
        msg_dic = {
            'cmd_type': cmd_type,
            'resp': resp,
            'currdir': currdir
        }
        msg_bytes = json.dumps(msg_dic).encode('utf-8')
        msg_length = struct.pack('i', len(msg_bytes))
        return msg_length, msg_bytes

    @staticmethod
    def file_header(cmd_type, filename, md5, filesize):
        header_dic = {
            'cmd_type': cmd_type,
            'filename': filename,
            'md5': md5,
            'filesize': filesize
        }
        header_bytes = json.dumps(header_dic).encode('utf-8')
        header_length = struct.pack('i', len(header_bytes))
        return header_length, header_bytes
