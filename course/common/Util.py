#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import os


def read_data(db_name):
    file = './db/{}.db'.format(db_name)
    if os.path.getsize(file) <= 0:
        lst = []
    else:
        fo = open(file, 'rb')
        lst = pickle.load(fo)
        fo.close()
    return lst


def getid(db_name):
    lst = read_data(db_name)
    if not lst:
        return 1;
    return len(lst) + 1


def save(db_name, obj):
    file = './db/{}.db'.format(db_name)
    lst = read_data(db_name)
    lst.append(obj)
    fw = open(file, 'wb')
    pickle.dump(lst, fw)
    fw.flush()
    fw.close()
    print("@-创建成功!")


def update(db_name, lst):
    file = './db/{}.db'.format(db_name)
    fw = open(file, 'wb')
    pickle.dump(lst, fw)
    fw.flush()
    fw.close()


def print_data(lst):
    for index, item in enumerate(lst):
        print(index, ":", item.__dict__)
    print("-----------------------")


def choose_school():
    print("@@@@@选择学校@@@@@")
    school_lst = read_data("school")
    if not school_lst:
        print("$-请先创建学校!")
        return
    print_data(school_lst)
    school_index = int(input("输入学校编号：").strip())
    school_id = getattr(school_lst[school_index], 'id')
    return school_id


def choose_teacher(school_id):
    print("@@@@@选择讲师@@@@@")
    teacher_lst = read_data("teacher")
    lst = []
    for item in teacher_lst:
        if getattr(item, 'school_id') == school_id:
            lst.append(item)
    if not lst:
        print("$-请先创建讲师!")
        return
    print_data(lst)
    teacher_index = int(input("输入讲师编号：").strip())
    teacher_id = getattr(lst[teacher_index], 'id')
    return teacher_id


def choose_course(school_id):
    print("@@@@@选择课程@@@@@")
    course_lst = read_data("course")
    lst = []
    for item in course_lst:
        if getattr(item, 'school_id') == school_id:
            lst.append(item)
    if not lst:
        print("$-需管理员创建课程!")
        return
    print_data(lst)
    class_index = int(input("输入课程编号：").strip())
    class_id = getattr(lst[class_index], 'id')
    return class_id


def choose_class_course(class_id):
    print("@@@@@选择课程@@@@@")
    class_lst = read_data("class")
    courses = []
    for item in class_lst:
        if getattr(item, 'id') == class_id:
            courses = getattr(item, 'courses')

    for i,v in enumerate(courses):
        print(i, ":", v)
    course_index = int(input("输入课程编号：").strip())
    course_id = courses[course_index]['course_id']
    return course_id


def choose_class(school_id):
    print("@@@@@选择班级@@@@@")
    class_lst = read_data("class")
    lst = []
    for item in class_lst:
        if getattr(item, 'school_id') == school_id:
            lst.append(item)
    if not lst:
        print("$-需管理员创建班级!")
        return
    print_data(lst)
    class_index = int(input("输入班级编号：").strip())
    class_id = getattr(lst[class_index], 'id')
    return class_id

