#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0.0
@author: yuolvv
@license: Apache Licence 
@file: TestSlots.py
@time: 2016/10/31 15:39
"""

class Student(object):
    pass

s = Student()
s.name = 'tsing'
print(s.name)

def set_age(self , age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)

s2 = Student()
#s2.set_age(25)

def set_score(self,score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
print(s.score)

s2.set_score(99)
print(s2.score)

class Student2(object):
    __slots__ = ('name','age')

s21 = Student2()
s21.name = 'song'
s.age = 23





