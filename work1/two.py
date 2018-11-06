menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车站':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}
flag = 0;
while True:
    # 一级
    for m1 in menu:
        print(m1)
    print("Z：退出")
    next1 = input("请选择菜单:")
    if(next1 == 'Z'):
        print("退出菜单")
        break
    if(next1 not in menu.keys()):
        print('菜单不存在')
        continue
    while True:
        for m2 in menu[next1]:
            print(m2)
        print("R：返回上级")
        print("Z：退出菜单")
        next2 = input("请选择菜单:")
        if(next2 == 'R'):
            print("返回上级菜单")
            break
        if (next2 == "Z"):
            print("退出菜单")
            flag = 1
            break
        if(next2 not in menu[next1].keys()):
            print('菜单不存在')
            continue
        while True:
            for m3 in menu[next1][next2].keys():
                print(m3)
            print("R：返回上级")
            print("Z：退出菜单")
            next3 = input("请选择菜单")
            if (next3 == "R"):
                print("返回上级菜单")
                break
            if (next3 == "Z"):
                print("退出菜单")
                flag = 1
                break
        if(flag == 1):
            break
    if (flag == 1):
        break