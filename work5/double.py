#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random as r
import time


class Chris:
    __base_list1 = list(range(1, 34))
    __base_list2 = list(range(1, 17))

    __base_data = []
    __count = []

    def __init__(self):
        self.read_data()

    def read_data(self):
        f = open('base_data', 'r')
        for line in f:
            list_temp = line.split(' ')
            m = list_temp.pop()
            index = list_temp.pop(0)
            n = list_temp
            tuple_temp = index, n, m.strip()
            self.__base_data.append(tuple_temp)
        f.close()
        self.__base_data.reverse()

    def choose(self, curr_data):
        #1
        base1 = list.copy(self.__base_list1)
        if len(base1) != 33:
            raise Exception("出错了")
        temp_data1 = []
        for i in range(6):
            for j in range(r.randint(0, 66)):
                r.shuffle(base1)
            n = base1.pop()
            temp_data1.append(n)
        temp_data1.sort()
        #2
        base2 = list.copy(self.__base_list2)
        if len(base2) != 16:
            raise Exception("出错了")
        temp_data2 = []
        for j in range(r.randint(0, 66)):
            r.shuffle(base2)
        m = base2.pop()
        temp_data2.append(m)
        if hash("".join(list(map(str, temp_data1)))) == hash("".join(curr_data[1])) and temp_data2[0] == curr_data[2]:
            print("Y:{}+{}, S:{}+{}".format(temp_data1, temp_data2[0], curr_data[1], curr_data[2]))
            return True
        else:
            return False

    def write_data(self, index, has_except=False):
        f = open("{}{}".format("temp/", index), "w+")
        start = index - 1000
        end = index
        if has_except:
            start = 0
            end = len(self.__count)
        for i in range(start, end):
            tmp = " ".join(tuple(map(str, self.__count[i]))) + "\n"
            f.write(tmp)
        f.flush()
        f.close()

    def getup(self):
        '''
        come on
        :return:
        '''
        i = 0
        for base in self.__base_data:
            index = base[0]
            data = base[1]
            cnt = 1
            while True:
                result = self.choose(base)
                if result:
                    tuple_temp = index, cnt, data
                    self.__count.append(tuple_temp)
                    print("^-^index:{},执行成功,总执行次数:{}".format(index, cnt))
                    if i % 666 == 0:
                        self.write_data(i)
                    break
                else:
                    cnt += 1
                if cnt % 6666 == 0:
                    print("·index:{},正在执行,已执行次数:{}".format(index, cnt))
            i += 0

    def go(self):
        '''
        go
        :return:
        '''
        try:
            self.getup()
        finally:
            self.write_data(int(time.time()), True)


chris = Chris()
chris.go()
