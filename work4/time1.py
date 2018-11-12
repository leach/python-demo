#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time

print(time.time())

print(time.localtime())

print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))

print(type(1541840737.3509588))

curr = time.gmtime()  # 当前时间戳 float    返回 元组time.struct_time
thisTime = time.gmtime(1541840737.3509588)  # 指定时间戳 float   返回 元组time.struct_time
date1 = time.strptime('2018-10-10', '%Y-%m-%d')       # 元组time.struct_time
datetime = time.strptime('2018-10-10 12:28:12', '%Y-%m-%d %H:%M:%S')  # 元组time.struct_time
dateTimeStr = time.strftime('%Y-%m-%d %H:%M:%S', date1)    # 2018-10-10 00:00:00
dateStr = time.strftime('%Y-%m-%d', datetime)               # 2018-10-10

print(curr)
print(thisTime)
print(date1)
print(datetime)
print(dateTimeStr)
print(dateStr)