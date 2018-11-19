#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os

from class2.exception import CommandException


class Querier:

    def __init__(self):
        self.data_path = "data/"
        self.datas = {}

    table_head = { 'staff': ['staff_id', 'name', 'age', 'phone', 'dept', 'enroll_date']}

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

    def filter(self, data_list, table, condition):
        filter_data = []
        heads = self.table_head[table]
        for data in data_list:
            for cond in condition:
                col = cond[0].strip()
                symbol = cond[1].strip()
                value = cond[2].strip()
                if col not in heads:
                    raise CommandException('查询数据语法错误')
                if not ((symbol == '>=' and data[col] >= value) or \
                        (symbol == '<=' and data[col] <= value) or \
                        (symbol == '=' and data[col] == value) or \
                        (symbol == '<' and data[col] < value) or \
                        (symbol == '>' and data[col] > value) or \
                        (symbol == 'like' and value in data[col])):
                    break;
            else:
                filter_data.append(data)
        return filter_data

    def find(self, command: list):
        table = command[0]
        column = command[1]
        condition = command[2]
        headers = self.table_head[table]
        filt_data = self.filter(self.datas[table], table, condition)
        if '*' in column:
            return filt_data
        result = []
        for d in filt_data:
            data = {}
            for col in column:
                col = col.strip()
                if col not in headers:
                    raise CommandException('查询数据语法错误')
                data[col] = d[col]
            result.append(data)
        return result

    def add(self, command: list):
        table = command[0]
        table_datas = self.datas[table]
        if len(table_datas) > 0:
            id = table_datas[-1][0] + 1
        else:
            id = 1
        command[1].insert(0, id)
        _data = command[1]
        table_datas.append(_data)

        for i in table_datas:
            print(i)
        pass

    def update(self, command: list):
        print('updateupdateupdate')
        pass

    def delete(self, command: list):
        print('deletedelete')
        pass

    def read_data(self, table):
        try:
            file = "{}{}".format(self.data_path, table)
            if not os.path.exists(file):
                self.datas[table] = []
                return
            _data = []
            f = open(file, 'r', encoding='utf-8')
            for line in f:
                info = dict(zip(self.table_head[table], line.strip().split(',')))
                _data.append(info)
            f.close()
            self.datas[table] = _data
        except IOError:
            raise CommandException("数据表不存在或查询失败")

    def exec(self, _command: str):
        """
        执行指令语法
        :param command: 指令
        :return:
        """
        #解析指令
        dic_cmd = self.__parse_command(_command)
        _table = dic_cmd['command'][0]
        if not dic_cmd:
            raise CommandException()
        #执行指令
        func = getattr(self, dic_cmd['type'])
        if func:
            self.read_data(_table)
            return func(dic_cmd['command'])
        else:
            raise CommandException()


    #测试
    def show(self):
        command1 = "find * from staff where age > 0 and name like 'W' "
        command2 = 'update staff set age=25 where name = "Alex Li"  and a like "331"'
        command3 = 'delete from staff where id=3'
        command4 = 'add kala Alex Li,25,134435344,IT,2015‐10‐29'
        command = [command4]  #, command2, command3, command4

        for c in command:
            staff_list = self.exec(c)
            if not staff_list:
                return
            for i in staff_list:
                print(i)




