
import os

f = open('02第二模块之三体语录.txt', 'r', encoding='utf-8')
fn = open('02第二模块之三体语录2.txt', 'w+', encoding='utf-8')

for index,line in enumerate(f.readlines()[:-1]):
    # if index == 2:
    #     line = line.replace('不要回答', '绝对不能回复')
        fn.write(line)
else:
    fn.write('给岁月以文明，而不是给文明以岁月\n')
f.close()
fn.close()

os.replace('02第二模块之三体语录2.txt', '02第二模块之三体语录.txt' )