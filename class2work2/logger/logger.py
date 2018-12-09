#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from logging import handlers


def account():
    log_file = 'log/account.log'
    return get_logger(log_file, "account")


def login():
    log_file = 'log/login.log'
    return get_logger(log_file, "login")


def get_logger(log_file, __name):
    logger = logging.getLogger(__name)
    fh = handlers.TimedRotatingFileHandler(filename=log_file, encoding='utf-8')
    formatter = logging.Formatter('[%(asctime)s %(module)s:%(funcName)s:%(lineno)d] %(levelname)s: %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    sh.setLevel(level=logging.INFO)
    logger.addHandler(sh)
    logger.setLevel(logging.INFO)
    return logger
