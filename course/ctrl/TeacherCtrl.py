#!/usr/bin/env python
# -*- coding: utf-8 -*-

from course.common import Util


class TeacherCtrl:

    @staticmethod
    def print_class(teacher_id):
        """
        查看班级
        :param teacher_id:
        :return:
        """
        lst = Util.read_data("class")
        new_lst = []
        for index, item in enumerate(lst):
            courses = getattr(item, "courses")
            for course in courses:
                if course['teacher_id'] == teacher_id:
                    new_lst.append(item)
                    print(index, ":", item.__dict__)
        print("-----------------")
        return new_lst

    @staticmethod
    def print_student(teacher_id):
        """
        查看学生
        :param teacher_id:
        :return:
        """
        print("@@@@@先选择班级@@@@@")
        class_lst = TeacherCtrl.print_class(teacher_id)
        n = int(input("输入班级编号：").strip())
        class_id = getattr(class_lst[n], 'id')
        lst = Util.read_data("student")
        new_lst = []
        print("@@@@@学生列表@@@@@")
        for index, item in enumerate(lst):
            if getattr(item, "class_id") == class_id:
                new_lst.append(item)
                print(index, ":", item.__dict__)
        print("-----------------")
        return new_lst

    @staticmethod
    def update_grade(teacher_id):
        student_lst = TeacherCtrl.print_student(teacher_id)
        n = int(input("输入学生编号：").strip())
        student = student_lst[n]
        student_id = getattr(student, 'id')

        course_id = Util.choose_class_course(getattr(student, 'class_id'))
        grade = int(input("输入分数:").strip())
        db_name = "student"
        lst = Util.read_data(db_name)
        for student in lst:
            if getattr(student, 'id') == student_id:
                if hasattr(student, 'grades'):
                    grades = getattr(student, 'grades')
                else:
                    grades = []
                for item in grades:
                    if item['course_id'] == course_id:
                        item['grade'] = grade
                        break
                else:
                    item = {'course_id': course_id, 'grade': grade}
                grades.append(item)
                setattr(student, 'grades', item)
        Util.update(db_name, lst)


