accounts = {}
try:
    f = open("accounts.conf")
    for line in f:
        info = line.strip().split(" ")
        accounts.update({info[0]: info})
finally:
    f.close()

try:
    df = open("locked.accounts", 'r', encoding='utf-8')
    for line in df:
        username = line.strip()
        accounts[username][2] = 1
finally:
    f.close()

print(accounts)
count = 0
lastUsername = ''
tryCount = 0
while count < 3:
    username = input("username:").strip()
    if(username in accounts):
        if accounts[username][2] == 1:
            print("用户已被锁定")
            continue
        password = input("password:").strip()
        if(password == accounts[username][1]):
            print("登陆成功")
            break
        else:
            if(lastUsername == username):
                tryCount += 1
            else:
                tryCount = 1
                lastUsername = username
            print("密码错误")
            if (tryCount == 3):
                print("账户锁定:", username)
                try:
                    ff = open("locked.accounts", 'w', encoding='utf-8')
                    ff.write(username)
                finally:
                    f.close()
    else:
        print("用户不存在")

    count += 1

else:
    print("操作次数过多")