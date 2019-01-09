#!/usr/bin/env python
# -*- coding: utf-8 -*-

from course.ctrl.StudentCtrl import StudentCtrl
from course.ctrl.TeacherCtrl import TeacherCtrl
from course.ctrl.Manage import Manage
from course.common import Util

stu_view = [('注册', 'create_student'), ('交学费', 'pay_fee')]
teach_view = [('查看班级', 'print_class'), ('查看学生', 'print_student'), ('修改成绩', 'update_grade')]
manage_view = [('创建学校', 'create_school'), ('创建讲师', 'create_teacher'), ('创建课程', 'create_course'), ('创建班级', 'create_class')]
main_view = [('学员操作', stu_view), ('讲师操作', teach_view), ('管理员操作', manage_view)]


def login(view_type):
    while True:
        print("-----登录-----")
        username = input('用户名:').strip();
        # password = input('密码:').strip(); #省去密码验证功能
        if view_type == 'm':
            if username == 'admin':
                break
            else:
                continue
        elif view_type == 's':
            lst = Util.read_data('student');
        elif view_type == 't':
            lst = Util.read_data('teacher');

        for v in lst:
            if username == getattr(v, 'name'):
                print("登录成功:", v.__dict__)
                return getattr(v, 'id');
        print("$-用户错误,重新登录!")


def main():
    for i,v in enumerate(main_view):
        print(i, ':', v[0])
    m = int(input('@@@@@选择操作：').strip())
    if m not in range(len(main_view)):
        print("$-选择错误!")
        return
    id = None
    if m == 0:
        ctrl = StudentCtrl
    elif m == 1:
        ctrl = TeacherCtrl
        #登录验证
        id = login('t')
    else:
        ctrl = Manage
        #登录验证
        id = login('m')
    second_view = main_view[m][1]

    while True:
        try:
            for i, v in enumerate(second_view):
                print(i, ':', v[0])
            n = int(input('@@@@@选择操作：').strip())

            if m == 0 and n == 1:
                # 登录验证
                id = login('s')

            targe_func = getattr(ctrl, second_view[n][1]);
            targe_func(id)

        except Exception:
                print("$-选择错误!")



main()

