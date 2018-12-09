#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import configparser
import datetime
from class2work2.login import login
from class2work2.logger import logger


class Account:
    CONSUME='消费'
    REPAYMENT='还款'
    TRANSFER='转账'
    GETCASH='提现'

    def __init__(self):
        self.logger = logger.account()
        self.default_config = ".\\account\\config.ini"
        parser = configparser.ConfigParser()
        parser.read(self.default_config)
        self.config = parser['DEFAULT']
        with open(self.config['account.path'], 'r', encoding='utf-8') as fp:
            self.infos = json.load(fp)

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Account, cls).__new__(cls)
        return cls.instance

    def get_info(self, username):
        if username in self.infos:
            return self.infos[username]
        return {}

    def get_amount(self, src, dst):
        amount = input("输入金额:").strip()
        try:
            amount = int(amount)
            if not amount:
                raise ValueError
        except ValueError:
            self.logger.warning("错误金额, FROM:%s, TO:%s, AMOUNT:%s", src, dst, amount)
            return None
        return amount

    @login.auth
    def consume(self, act_name, amount, goodslist):
        act = self.get_info(act_name)
        act['rest'] = act['rest'] - amount
        if act['rest'] < amount:
            self.logger.warning("余额不足, ACCOUNT:%s, AMOUNT:%s", act_name, amount)
            return False
        self.infos[act_name] = act
        self.record(act_name, None, amount, Account.CONSUME, goodslist)
        return True

    @login.auth
    def transfer(self, src):
        dst = input("输入对方账户:").strip()
        amount = self.get_amount(src, dst)
        if not amount:
            return False
        src_act = self.get_info(src)
        dst_act = self.get_info(dst)
        if not src_act or not dst_act:
            self.logger.warning("账户不存在, FROM:%s, TO:%s, AMOUNT:%s", src, dst, amount)
            return False
        if src_act['rest'] < amount:
            self.logger.warning("余额不足, FROM:%s, TO:%s, AMOUNT:%s", src, dst, amount)
            return False
        src_act['rest'] = src_act['rest'] - amount
        dst_act['rest'] = dst_act['rest'] + amount
        self.infos[src] = src_act
        self.infos[dst] = dst_act
        self.record(src, dst, amount, Account.TRANSFER)
        return True

    @login.auth
    def repayment(self, act_name):
        amount = self.get_amount(act_name, None)
        if not amount:
            return False
        act = self.get_info(act_name)
        act['rest'] = act['rest'] + amount
        self.infos[act_name] = act
        self.record(act_name, None, amount, Account.REPAYMENT)
        return True

    @login.auth
    def getcash(self, act_name):
        act = self.get_info(act_name)
        amount = self.get_amount(act_name, None)
        if not amount:
            return False
        fee = amount * 0.05
        if act['rest'] < (fee + amount):
            self.logger.warning("余额不足, ACCOUNT:%s, AMOUNT:%s", act_name, amount)
            return False
        act['rest'] = act['rest'] - amount - fee
        self.record(act_name, None, amount, Account.GETCASH)
        return True

    def record(self, src, dst, amount, type, *goodslist):
        '''
        记录流水
        :param src:
        :param dst:
        :param amount:
        :param type:
        :param goodslist:
        :return:
        '''
        item = {}
        d = datetime.datetime.now()
        item.setdefault("date", d.today())
        item.setdefault("from", src)
        item.setdefault("to", dst)
        item.setdefault("amount", amount)
        item.setdefault("type", type)
        item.setdefault("goodslist", goodslist)
        act = self.get_info(src)
        act['billlist'].append(item)
        self.infos[src] = act
        self.logger.info("%s, FROM:%s, TO:%s, AMOUNT:%s", type, src, dst, amount)
        return True

