goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998}
]

#读取账户
accounts = {}    #{'hello': {'password': 'world', 'balance': 100, 'carts': []}}
accounts_file = open('accounts')
accounts = eval(accounts_file.read())

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
curr_user['balance'] = input_salary

while True:
    # 展示商品
    print("请选择商品：")
    for v in goods:
        i = goods.index(v)
        print(i + 1, '商品名:', v['name'], '价格:', v['price'])
    # 选择商品
    choice = input('请选择:').strip()
    if choice == 'q':
        #展示已购买商品
        print("-------已购买商品-------")
        for v in curr_user['carts']:
            print("商品名:", v['name'], "价格:", v['price'], "购买数量:", v['count'])
        print("------------------------")
        print("退出系统")
        break
    #购买
    if int(choice) in range(1, len(goods) + 1):
        goodsNum = int(choice) - 1
        if curr_user['balance'] - goods[goodsNum]['price'] >= 0:
            _goods = goods[goodsNum]
            curr_user['balance'] -= goods[goodsNum]['price']
            if(curr_user['carts'].count(goods[goodsNum]) > 0):
                for v in curr_user['carts']:
                    if(_goods['name'] == v['name']):
                        _goods['count'] = v['count'] + 1
                        curr_user['carts'].remove(v)
                        curr_user['carts'].append(_goods)
            else:
                _goods['count'] = 1
                curr_user['carts'].append(_goods)
            print("已购买商品:", _goods['name'], "价格:", _goods['price'], "账户余额:", curr_user['balance'])
        else:
            print('余额不足')
    else:
        print("没有此商品")

# 保存accounts
accounts.update({input_user: accounts[input_user]})
try:
    ff = open("accounts", 'w', encoding='utf-8')
    ff.write(str(accounts))
finally:
    ff.close()




