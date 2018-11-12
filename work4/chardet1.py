
import chardet
#
# ff = open('test', 'w+', encoding='gbk ')
# ff.write('测试')
# ff.close()
#
#
# f = open('test', 'rb')
# data = f.read()
# print(data.decode('KOI8-R'))
# r = chardet.detect(data)
# f.close()
# print(r)

#
# s = b'\xb2\xe2\xca\xd4'.decode(encoding="gbk")
# print(s)
#
# d = '测试'.encode('gbk')
# print(d)
#
# fff = open('test', 'wb')
# fff.write('Русский '.encode("KOI8-R"))
# fff.close()
#
# ffff = open('foo', 'ab')
# ffff.write("你好啊".encode('gbk'))
# ffff.close()


# f = open('foo', 'r+')
# data = f.read()
# print(data)
#
# f.write('\n再写几个字')
# f.close()

f = open('foo', 'w+')
data = f.read()
print(data)

f.write('\n再写几个字')
f.close()