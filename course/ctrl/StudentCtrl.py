#!/usr/bin/env python
# -*- coding: utf-8 -*-

from course.obj.Obj import *
from course.common import Util


class StudentCtrl:

    @staticmethod
    def create_student(mark):
        """
        5. 创建学员时，选择学校，关联班级
        :return:
        """
        db_name = "student"
        print("-----学员注册:-----")
        name = input("姓名：").strip()
        school_id = Util.choose_school()
        if not school_id:
            return
        class_id = Util.choose_class(school_id)
        if not class_id:
            return
        id = Util.getid(db_name)
        obj = Student(id, name, school_id, class_id)
        Util.save(db_name, obj)

    @staticmethod
    def pay_fee(student_id):
        """
        交学费
        :return:
        """
        db_name = "student"
        lst = Util.read_data(db_name)
        for student in lst:
            if getattr(student, 'id') == student_id:
                setattr(student, 'fee_ispaid', True)
        Util.update(db_name, lst)
        print("@-缴费成功!")
