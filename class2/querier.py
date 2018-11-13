#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class Querier:

    def __init__(self, data_file):
        self.data_file = data_file

    pattern_table = 'from(.*)where'  # 取表
    pattern_column = 'find(.*)from'  # 取字段
    pattern_condition = 'where(.*)'  # 取条件

    def __parsefind(self, command: str):
        print(command)
        table = re.sub('from|where', '', re.search(self.pattern_table, command).group()).strip()
        column = re.sub('from|find| ', '', re.search(self.pattern_column, command).group()).strip().split(',')
        condition = re.sub('where| ', '', re.search(self.pattern_condition, command).group()).strip().split('and')
        print(condition)

    def __parseadd(self, command: str):
        print("add")

    def __parseupdate(self, command: str):
        print("update")

    def __parsedelete(self, command: str):
        print("delete")

    dict_switch = {
        "find": __parsefind,
        "add": __parseadd,
        "update": __parseupdate,
        "delete": __parsedelete
    }

    # 解析查询指令
    def __parsecommand(self, command: str, type):
        return self.dict_switch[type](self, command.strip().replace("\n", ""))

    #测试
    def show(self):
        command = '''
        find name,   age from 
        staff_table where age > 22 and name = 2
        '''
        self.__parsecommand(command, "find")
        # try:
        #     f = open(self.data_file, 'r')
        #     for line in f:
        #         print(line.strip())
        #     f.close()
        # except IOError:
        #     print("Error: 没有找到文件或读取文件失败")


