#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser as parser
import random, string
from ftp.server.config.Settings import ServerSettings
from ftp.server.auth.FtpUser import FtpUser
from ftp.common.Exception import CmdException
from ftp.server.tool.Tools import PWDTool


class AuthManage:
    """
    登录管理
    """

    def __init__(self):
        config = parser.ConfigParser()
        config.read(ServerSettings.ACCOUNT_FILE_PATH)
        self.config = config
        self.store = {}

    def login(self, username, password):
        conf = self.config
        if not conf.__contains__(username):
            raise CmdException("$用户不存在")
        user_conf = conf[username]
        if user_conf['password'] == PWDTool.md5(password):
            homedir = user_conf['homedir']
            maxsize = user_conf['maxsize']
            usedsize = user_conf['usedsize']
            ftpuser = FtpUser(username, homedir, homedir, maxsize, usedsize)
            auth = ''.join(random.sample(string.ascii_letters + string.digits, 8))
            self.store[auth] = ftpuser
            return auth, homedir, homedir
        else:
            raise CmdException("$用户密码错误")
