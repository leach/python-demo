#!/usr/bin/env python
# -*- coding: utf-8 -*-
goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998}
]

#读取账户
with open('cart.txt', 'r', encoding='utf-8') as f:
    accounts = eval(f.read())   #{'hello': {'password': 'world', 'balance': 100, 'carts': []}}
    f.close()
# 登录
input_user = input("username:").strip()
if input_user not in accounts.keys():
    print('用户名不存在')
    exit()
# 当前用户信息
curr_user = accounts[input_user]
# 录入密码
input_passwd = input("password:").strip()
if input_passwd != curr_user['password']:
    print('密码不对')
    exit()

print("欢迎进入购物系统")
input_salary = int(input("salary:").strip())
# 存储工资
curr_user['balance'] = curr_user.get('balance', 0) + input_salary

while True:
    # 展示商品
    print("请选择商品：")
    for v in goods:
        i = goods.index(v)
        print(i, '商品名:', v['name'], '价格:', v['price'])
    # 选择商品
    choice = input('请选择:').strip()
    if choice == 'q':
        #展示已购买商品1
        1
        for v in curr_user['carts']:
            print("商品名:%s 价格:%s 购买数量:%s" % (v['name'], v['price'], v['count']))
        print("账户余额: %s" % (curr_user['balance']))
        print("退出系统")
        break
    #购买
    if int(choice) in range(len(goods)):
        goodsNum = int(choice)
        if curr_user['balance'] - goods[goodsNum]['price'] >= 0:
            _goods = goods[goodsNum]
            curr_user['balance'] -= goods[goodsNum]['price']
            #更新已购买数量
            if curr_user['carts'].count(goods[goodsNum]) > 0:
                index = curr_user['carts'].index(goods[goodsNum])
                tempGoods = curr_user['carts'][index]
                _goods['count'] = tempGoods['count'] + 1
                curr_user['carts'].remove(tempGoods)
            else:
                _goods['count'] = 1
            curr_user['carts'].append(_goods)
            print("已购买商品:", _goods['name'], "价格:", _goods['price'], "账户余额:", curr_user['balance'])
        else:
            print('余额不足')
    else:
        print('\033[1;37;40m没有此商品！\033[0m')

# 保存accounts
with open("cart.txt", 'w', encoding='utf-8') as ff:
    ff.write(str(accounts))
    ff.close()

