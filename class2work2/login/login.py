#!/usr/bin/env python
# -*- coding: utf-8 -*-

from class2work2.logger import logger
import json

logger = logger.login()
__hadAuth = []


def auth(func):
    def wrapper(cls, username, *args, **kwargs):
        if username in __hadAuth:
            return func(cls, username, *args, **kwargs)
        password = input('用户【{}】登录,输入密码:\n'.format(username)).strip()
        infos = get_account_info()
        if username not in infos.keys():
            logger.info("账号错误,登录失败")
            return False
        info = infos[username]
        if not info or info['password'] != password:
            logger.info("账号错误,登录失败")
            return False
        __hadAuth.append(username)
        logger.info("登录成功")
        return func(cls, username, *args, **kwargs)
    return wrapper


def get_account_info():
    with open("./account/account.json", 'r', encoding='utf-8') as fp:
        infos = json.load(fp)
    return infos


def logout(username):
    __hadAuth.remove(username)
    logger.info("用户【%s】退出".format(username))
