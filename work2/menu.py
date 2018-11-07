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
#当前菜单
tempMenu = [menu]
while True:
    menuLen = len(tempMenu)
    if menuLen < 1:
        print("菜单丢了!")
    #打印当前菜单
    for v in tempMenu[menuLen - 1]:
        print(v)
    #输入选择
    choice = input("选>").strip()
    #退出操作
    if choice == "q":
        print("退出!")
        break
    #返回上级
    if choice == "l":
        if menuLen > 1:
            tempMenu.remove(tempMenu[menuLen - 1])
        else:
            print("到顶了!")
        continue
    #更新当前菜单
    if choice in tempMenu[menuLen - 1].keys():
        if len(tempMenu[menuLen - 1][choice].keys()) == 0:
            print("到底了!")
        else:
            tempMenu.append(tempMenu[menuLen - 1][choice])
    else:
        print("选择错了!")
