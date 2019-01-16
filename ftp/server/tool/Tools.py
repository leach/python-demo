#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, hashlib, os
from ftp.common.Exception import CmdException


class PathTool:

    @staticmethod
    def pathhandler(homedir: str, currdir: str, dstdir: str):
        """
        处理目录路径
        :param homedir:
        :param currdir:
        :param dstdir:
        :return:
        """
        if not re.findall("[^.].*", dstdir):
            raise CmdException("$没有目录权限")
        if dstdir.startswith("../"):
            dstdirs = re.subn('(\.\./)', '', dstdir)
            dstdir_name = dstdirs[0]
            count = dstdirs[1]
            currdirs = currdir.split("/")
            parent_dir = "/".join(currdirs[0:-count])
            if parent_dir == "" and not (dstdir_name.startswith(homedir[1:] + "/") or dstdir_name == homedir[1:]):
                raise CmdException("$没有目录权限")
            if dstdir_name:
                dstdir_path = parent_dir + "/" + dstdir_name
            else:
                dstdir_path = parent_dir
        elif dstdir.startswith("/"):
            if dstdir == homedir or dstdir.startswith(homedir + "/"):
                dstdir_path = dstdir
            else:
                raise CmdException("$没有目录权限")
        elif dstdir.startswith("./"):
            dstdir_name = re.findall("[^./].*", dstdir)
            if dstdir_name:
                dstdir_path = currdir + "/" + dstdir_name[0]
            else:
                dstdir_path = currdir
        else:
            dstdir_path = currdir + "/" + dstdir
        return dstdir_path


class PWDTool:

    @staticmethod
    def md5(arg):
        """
        加密密码
        :param arg:
        :return:
        """
        md5_pwd = hashlib.md5(bytes('adfhjl', encoding='utf-8'))
        md5_pwd.update(bytes(arg, encoding='utf-8'))
        return md5_pwd.hexdigest()

# print(MD5Tool.md5('ftp'))
