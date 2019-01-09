#!/usr/bin/env python
# -*- coding: utf-8 -*-


class School:
    """
    学校对象
    """
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address


class Class:
    """
    班级
    """
    def __init__(self, id, name, school_id, courses):
        self.id = id
        self.name = name
        self.school_id = school_id
        self.courses = courses


class Teacher:
    """
    讲师
    """
    def __init__(self, id, name, school_id):
        self.id = id
        self.name = name
        self.school_id = school_id


class Course:
    """
    课程对象
    """
    def __init__(self, id, name, cycle, price, school_id):
        self.id = id
        self.name = name
        self.cycle = cycle
        self.price = price
        self.school_id = school_id


class Student:
    """
    学员
    """
    def __init__(self, id, name, school_id, class_id):
        self.id = id
        self.name = name
        self.school_id = school_id
        self.class_id = class_id
        self.grades = []
