#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


# 读取账户
def read_accounts(file: str):
    accounts = {}
    fo = open(file, 'r', encoding='utf-8')
    for line in fo:
        account = line.strip().split(" ")
        accounts.update({account[0]: account})
    fo.close()
    return accounts


# 锁定账户
def update_accounts(file, accounts):
    fo = open(file, 'w+', encoding='utf-8')
    for i in accounts:
        account = accounts[i]
        print(account)
        line = ' '.join(account) + '\n'
        fo.write(line)
    fo.close()


def login():
    accounts_file = 'accounts.txt'
    accounts = read_accounts(accounts_file)
    while True:
        username = input("输入用户名:").strip()
        if username == 'q':
            print("退出!")
            break
        if username not in accounts.keys():
            print("用户名不存在!")
            continue
        if int(accounts[username][2]) == 0:
            print("用户已被锁定!")
            continue

        for count in range(3):
            password = input("输入密码:").strip()
            if password != accounts[username][1]:
                print("密码错误!")
                if count == 2:
                    print("密码错误3次,账户锁定!")
                    accounts[username][2] = '0'
                    break
            else:
                print("登录成功!")
                break

    update_accounts(accounts_file, accounts)


# 登录
login()

