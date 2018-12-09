#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from class2work2.account.account import Account
from class2work2.login import login


class Shop:

    def __init__(self):
        with open('./shop/goods.json', 'r', encoding='utf-8') as fp:
            self.goodslist = json.load(fp)
        self.carts = []

    def show_goods(self):
        for index,item in enumerate(self.goodslist):
            print(index, item['name'],'价格', item['price'])

    def add_cart(self, goods):
        goods_name = goods['name']
        for item in self.carts:
            if item['name'] == goods_name:
                item['count'] = item['count'] + 1
                return
        else:
            _goods = dict.copy(goods)
            _goods['count']  = 1
            self.carts.append(_goods)

    @login.auth
    def settle_cart(self, username):
        amount = 0
        for item in self.carts:
            amount = amount + item['count']*item['price']
        account = Account()
        return account.consume(username, amount, self.carts)

    @login.auth
    def buy(self, username):
        while True:
            self.show_goods()
            choose = int(input("选择商品加购物车:").strip())
            if choose < 0:
                print("购物车结算中...")
                feedback = self.settle_cart(username)
                if feedback:
                    print("购物成功!")
                else:
                    print("结算失败!")
                return
            if choose >= len(self.goodslist):
                print("选择错误!")
                return self.buy()
            self.add_cart(self.goodslist[choose])
