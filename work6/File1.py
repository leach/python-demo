import os
fo = open("02第二模块之三体语录.txt", "r", encoding="utf-8")
fo_new = open("02第二模块之三体语录.txt.2", "w", encoding="utf-8")
# fo.seek(10)
# a = fo.read(3)
# print(a)


for index,line in enumerate(fo):
    if index == 2:
        line = line.replace("不要回答", "绝对不能回复");
    fo_new.write(line)

fo.close()
fo_new.close()

os.replace("02第二模块之三体语录.txt.2", "02第二模块之三体语录.txt")