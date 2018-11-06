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
currLevel = menu
lastLevel = menu
while True:
    #打印当前菜单
    for v in currLevel:
        print(v)
    #输入选择
    choice = input("选>").strip()
    #退出操作
    if choice == "q":
        print("退出!")
        break
    #返回上级
    if choice == "l":
        currLevel = lastLevel
        continue
    #更新当前菜单
    if choice in currLevel.keys():
        if len(currLevel[choice].keys()) == 0:
            print("到底了!")
        else:
            lastLevel = currLevel
            currLevel = currLevel[choice]
    else:
        print("选择错了!")
