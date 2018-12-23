
import os

fo = open("02第二模块之三体语录.txt", "r", encoding="utf-8")

lines = fo.readlines()

fw = open("02第二模块之三体语录.txt", "w", encoding="utf-8")
for index,line in enumerate(lines[0:-1]):
    if index == 4:
        fw.write("给岁月以文明，而不是给文明以岁月\n")
    fw.write(line)

fo.close()
fw.close()
