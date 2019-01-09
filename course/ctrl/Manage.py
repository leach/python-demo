#!/usr/bin/env python
# -*- coding: utf-8 -*-

from course.obj.Obj import *
from course.common import Util


class Manage:

    @staticmethod
    def create_school(mark):
        db_name = "school"
        print("-----创建学校:-----")
        name = input("名称：").strip()
        address = input("地址：").strip()
        id = Util.getid(db_name)
        obj = School(id, name, address)
        Util.save(db_name, obj)

    @staticmethod
    def create_teacher(mark):
        """
        创建讲师角色时要关联学校
        :return:
        """
        db_name = "teacher"
        print("-----创建讲师:-----")
        name = input("姓名：").strip()
        school_id = Util.choose_school()
        if not school_id:
            return
        id = Util.getid(db_name)
        obj = Teacher(id, name, school_id)
        Util.save(db_name, obj)

    @staticmethod
    def create_course(mark):
        """
        课程包含，周期，价格，通过学校创建课程
        :return:
        """
        db_name = "course"
        print("-----创建课程:-----")
        name = input("课程名：").strip()
        cycle = input("周期：").strip()
        price = input("学费：").strip()
        school_id = Util.choose_school()
        if not school_id:
            return
        id = Util.getid(db_name)
        obj = Course(id, name, cycle, price, school_id)
        Util.save(db_name, obj)

    @staticmethod
    def create_class(mark):
        """
        通过学校创建班级， 班级关联课程、讲师
        :return:
        """
        db_name = "class"
        print("-----创建班级:-----")
        name = input("名称：").strip()
        school_id = Util.choose_school()
        if not school_id:
            return
        courses = []
        while True:
            course_id = Util.choose_course(school_id)
            teacher_id = Util.choose_teacher(school_id)
            if not course_id or not teacher_id:
                print("$-选择错误!")
            cou = {"course_id": course_id, "teacher_id": teacher_id}
            courses.append(cou)
            n = input("输入1继续选择课程与教师:")
            if n != 1:
                break
        id = Util.getid(db_name)
        obj = Class(id, name, school_id, courses)
        Util.save(db_name, obj)
