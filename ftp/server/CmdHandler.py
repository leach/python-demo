#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ftp.common.Tools import MD5Tool
from ftp.server.auth.AuthManage import AuthManage
from ftp.server.auth.FtpUser import FtpUser
from ftp.server.config.Settings import ServerSettings
from ftp.common.Message import Message
from ftp.server.tool.Tools import PathTool
from ftp.common.Exception import CmdException
import socket, hashlib, json, struct, os


class CmdHandler:
    base_dir = ServerSettings.FTP_SERVER_BASE_DIR_PATH

    @staticmethod
    def handler(conn, req_bytes, authmanage: AuthManage):
        """
        handler
        :param conn:
        :param req_bytes:
        :param authmanage:
        :return:
        """
        req_dict = json.loads(req_bytes.decode('utf-8'))
        if 'cmd' in req_dict.keys():
            cmd_dict = req_dict['cmd'].split()
            cmd = cmd_dict[0]
            if cmd == 'close':
                conn.close()
                return
        if 'auth' not in req_dict.keys():
            auth, homedir, currdir = authmanage.login(req_dict['username'], req_dict['password'])
            if auth:
                CmdHandler.__authsuccess(conn, auth, homedir, currdir)
            return
        # 校验登录
        auth = req_dict['auth']
        if auth not in authmanage.store.keys():
            raise CmdException("$用户登录失效")
        # 用户已登录，处理命令：
        ftpuser = authmanage.store[auth]
        if len(cmd_dict) == 2:
            args = cmd_dict[1]
        else:
            args = None
        if cmd == 'get':
            resp = CmdHandler.__downloadfile(ftpuser, conn, args)
            return
        elif cmd == 'cd':
            resp = CmdHandler.__changedir(ftpuser, args)
        elif cmd == 'ls':
            resp = CmdHandler.__listdir(ftpuser, args)
        elif cmd == 'mkdir':
            resp = CmdHandler.__makedir(ftpuser, args)
        elif cmd == 'del':
            resp = CmdHandler.__deletefile(ftpuser, args)
        elif cmd == 'put':
            resp = CmdHandler.__putfile(ftpuser, conn, args)
            return
        # 返回成功结果
        currdir = ftpuser.currdir
        msg_length, msg_bytes = Message.succ_resp_header(cmd, resp, currdir)
        conn.send(msg_length)
        conn.send(msg_bytes)

    @staticmethod
    def __authsuccess(conn, auth, homedir, currdir):
        header_length, header_bytes = Message.login_success_msg(auth, homedir, currdir)
        conn.send(header_length)
        conn.send(header_bytes)

    @staticmethod
    def __changedir(ftpuser: FtpUser, dstdir: str):
        """
        切换目录
        :param ftpuser:  登录用户
        :param dstdir:   切换目录
        :return:
        """
        base_dir = ServerSettings.FTP_SERVER_BASE_DIR_PATH;
        homedir = ftpuser.homedir
        currdir = ftpuser.currdir
        dstdir_path = PathTool.pathhandler(homedir, currdir, dstdir)
        abs_path = base_dir + dstdir_path
        if not os.path.isdir(abs_path):
            raise CmdException("$目录不存在")
        if dstdir_path.endswith("/"):
            dstdir_path = dstdir_path[0:-1]
        setattr(ftpuser, 'currdir', dstdir_path)
        return True

    @staticmethod
    def __makedir(ftpuser: FtpUser, newdir: str):
        """
        创建目录
        :param ftpuser:  登录用户
        :param newdir:   新目录
        :return:
        """
        base_dir = ServerSettings.FTP_SERVER_BASE_DIR_PATH;
        currdir = ftpuser.currdir
        newdir_path = base_dir + currdir + "/" + newdir
        if os.path.exists(newdir_path):
            raise CmdException("$目录已存在")
        os.mkdir(newdir_path)
        return True

    @staticmethod
    def __listdir(ftpuser: FtpUser, lstdir: str):
        homedir = ftpuser.homedir
        currdir = ftpuser.currdir
        if lstdir:
            lstdir_path = PathTool.pathhandler(homedir, currdir, lstdir)
        else:
            lstdir_path = ftpuser.currdir
        abs_path = ServerSettings.FTP_SERVER_BASE_DIR_PATH + lstdir_path
        lst = os.listdir(abs_path)
        for i,item in enumerate(lst):
            if os.path.isdir(os.path.join(abs_path, item)):
                item = '\033[31m{}\033[0m'.format(item)
                lst[i] = item
        return lst

    @staticmethod
    def __deletefile(ftpuser: FtpUser, filename: str):
        """
        删除文件、目录
        :param ftpuser:
        :param filename:
        :return:
        """
        abs_path = ServerSettings.FTP_SERVER_BASE_DIR_PATH + ftpuser.currdir
        file_path = os.path.join(abs_path, filename)
        if not os.path.exists(file_path):
            raise CmdException("$文件不存在")
        else:
            if os.path.isdir(file_path):
                os.removedirs(file_path)
            else:
                os.remove(file_path)
        return True;

    @staticmethod
    def __downloadfile(ftpuser: FtpUser, conn: socket, filename: str):
        """
        下载文件
        :param ftpuser:
        :param conn:
        :param filename:
        :return:
        """
        currdir = ftpuser.currdir
        abs_path = ServerSettings.FTP_SERVER_BASE_DIR_PATH + currdir
        file_path = os.path.join(abs_path, filename)
        if not os.path.exists(file_path):
            raise CmdException("$文件不存在")
        filesize = os.path.getsize(file_path)
        md5 = MD5Tool.getfilemd5(file_path)
        header_length, header_bytes = Message.file_header('get', filename, md5, filesize)
        # 报头长度
        conn.send(header_length)
        # 报头
        conn.send(header_bytes)
        # 发送真是数据
        with open(file_path, 'rb') as f:
            for line in f:
                conn.send(line)
        return True

    @staticmethod
    def __putfile(ftpuser: FtpUser, conn: socket, filename: str):
        """
        上传文件
        :param ftpuser:
        :param conn:
        :param filename:
        :return:
        """
        # 报头长度
        obj = conn.recv(4)
        if not obj: raise CmdException("$报文为空")
        header_size = struct.unpack('i', obj)[0]
        # 报头
        header_bytes = conn.recv(header_size)
        # 解析报头
        header_dic = json.loads(header_bytes.decode('utf-8'))

        total_size = header_dic['filesize']
        filename = header_dic['filename']
        file_path = os.path.join(ServerSettings.FTP_SERVER_BASE_DIR_PATH + ftpuser.currdir, filename)
        if os.path.isfile(file_path):
            header_length, header_bytes = Message.error_resp_header("$文件已存在")
            conn.send(header_length)
            conn.send(header_bytes)
            return
        else:
            msg_length, msg_bytes = Message.succ_resp_header('put', None, ftpuser.currdir)
            conn.send(msg_length)
            conn.send(msg_bytes)
        # 接收数据
        with open(file_path, 'wb') as f:
            recv_size = 0
            while recv_size < total_size:
                line = conn.recv(8096)
                f.write(line)
                recv_size += len(line)
            f.flush()
            f.close()
        return True
