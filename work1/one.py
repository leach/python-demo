accounts = { 'alex': 'alex', 'luke': 'luke', 'dog': 'dog'}

count = 0
while count < 3:
    username = input("username:").strip()
    if(username in accounts):
        password = input("password:").strip()
        if(password == accounts[username]):
            print("登陆成功")
            break
        else:
            print("密码错误")
    else:
        print("用户不存在")

    count += 1

else:
    print("操作次数过多")