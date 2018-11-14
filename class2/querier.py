#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from class2.exception import CommandException


class Querier:

    def __init__(self, data_file):
        self.data_file = data_file

    def __split_condition(self, condition):
        """
        处理where条件
        :param condition: 条件
        :return: 条件列表
        """
        symbols = ['>=', '<=', '=', ' like ', '>', '<']
        new_condition = []
        for cond in condition:
            for symbol in symbols:
                conds = cond.strip().split(symbol)
                if len(conds) == 2:
                    if '\"' in conds[1] or '\'' in conds[1]:
                        conds[1] = re.findall('[\"|\'](.*)[\"|\']', conds[1].strip())[0]  #处理字符串的引号
                    conds.insert(1, symbol)
                    new_condition.append(conds)
                    break
        if len(new_condition) != len(condition):
            raise CommandException('条件语句错误')
        return new_condition

    def __parse_find(self, command: str):
        """
        处理查询指令语法
        :param command: 指令
        :return:
        """
        table = re.findall(".*from(.*)where.*", command)[0].strip()
        column = re.findall(".*find(.*)from.*", command)[0].strip().split(',')
        condition_str = re.findall("where(.*)", command)[0].strip().split('and')
        #处理字段
        for i, col in enumerate(column):
            if ' ' in col.strip() or not col.strip():
                raise CommandException('查询数据语法错误')
            column[i] = col.strip()
        condition = self.__split_condition(condition_str)
        return table, column, condition

    def __parse_add(self, command: str):
        """
        处理新增数据语法
        :param command: 指令
        :return:
        """
        separate = re.subn('add', '', command)
        if separate[1] != 1:
            raise CommandException('新增数据语法错误')
        line = separate[0].strip();
        table = re.search('[^\s]*[\s]', line).group().strip()
        add_value = re.search('[\s](.*)', line).group().strip().split(',')
        return table, add_value

    def __parse_update(self, command: str):
        """
        处理更新数据语法
        :param command:
        :return:
        """
        table = re.findall("update(.*)set.*", command)[0].strip()
        set_value_str = re.findall("set(.*)where.*", command)[0].strip().split(',')
        condition_str = re.findall(".*where(.*)", command)[0].strip().split('and')
        condition = self.__split_condition(condition_str)
        set_value = []
        for v in set_value_str:
            set_value.append(v.strip().split('='))
        return table, set_value, condition

    def __parse_delete(self, command: str):
        """
        处理删除数据语法
        :param command:
        :return:
        """
        table = re.findall("from(.*)where.*", command)[0].strip()
        condition_str = re.findall("where(.*)", command)[0].strip().split('and')
        condition = self.__split_condition(condition_str)
        return table, condition

    dict_parse_switch = {
        "find": __parse_find,
        "add": __parse_add,
        "update": __parse_update,
        "delete": __parse_delete
    }

    def __parse_command(self, _command: str):
        """
        解析各种指令、查询数据
        :param _command:
        :return:
        """
        command = _command.strip().replace("\n", "")
        _type = re.search('[^\s]*[\s]', command).group().strip()
        dic = {'type': _type}
        try:
            dic['command'] = self.dict_parse_switch[_type](self, command)
        except CommandException as e:
            print("{}:{}".format(e.message, command))
            return None
        except KeyError:
            print("指令语法错误:{}".format(command))
            return None
        return dic

    def find(self, command: list):
        print('ffffffind')

    def add(self, command: list):
        print('addaddadd')
        pass

    def update(self, command: list):
        print('updateupdateupdate')
        pass

    def delete(self, command: list):
        print('deletedelete')
        pass

    def read_data(self):
        print('读取数据')

    def exec(self, _command: str):
        """
        执行指令语法
        :param command: 指令
        :return:
        """
        #解析指令
        dic_cmd = self.__parse_command(_command)
        if not dic_cmd:
            raise CommandException()
        #执行指令
        func = getattr(self, dic_cmd['type'])
        if func:
            self.read_data()
            func(dic_cmd['command'])
        else:
            raise CommandException()


    #测试
    def show(self):
        command1 = "find name, age from staff_table where age > 22 and a like '331'"
        command2 = 'update staff_table set age=25 where name = "Alex Li"  and a like "331"'
        command3 = 'delete from staff where id=3'
        command4 = 'add staff_table Alex Li,25,134435344,IT,2015‐10‐29'
        command = [command1, command2, command3, command4]

        for c in command:
            self.exec(c)

        # try:
        #     f = open(self.data_file, 'r')
        #     for line in f:
        #         print(line.strip())
        #     f.close()
        # except IOError:
        #     print("Error: 没有找到文件或读取文件失败")


