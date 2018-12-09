#!/usr/bin/env python
# -*- coding: utf-8 -*-

from class2work2.shop.shop import Shop
from class2work2.account.account import Account

account = Account()
menu = ['购物商场', 'ATM']
atm_menu = ['转账', '还款', '提现']

while True:
    print("welcome!")
    for index, item in enumerate(menu):
        print(index, item)
    try:
        choose = int(input("选择进入系统:").strip())
        if choose not in range(2):
            raise ValueError
        username = input("输入账户:").strip()
        if choose == 0:
            print("进入购物商城!")
            shop = Shop()
            shop.buy(username)
        else:
            for index,item in enumerate(atm_menu):
                print(index, item)
            choose = int(input("选择ATM功能:").strip())
            if choose not in range(2):
                raise ValueError
            if choose == 0:
                account.transfer(username)
            elif choose == 1:
                account.repayment(username)
            elif choose == 2:
                account.getcash(username)
            else:
                raise ValueError
    except ValueError:
        print("选择错误!")
        continue



