#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0.0
@author: yuolvv
@license: Apache Licence 
@file: TestObjectInfo.py
@time: 2016/10/31 14:57
"""

print(type(123))
print(type('123'))
print(type(None))
print(type(abs))

class Animal(object):
    def run(self):
        print("Animal is running...")

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Husky(Dog):
    def run(self):
        print('Husky is running...')

a = Animal()
d = Dog()
h = Husky()

# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上
print(isinstance(h,Husky))
print(isinstance(h,Dog))
print(isinstance(h,Animal))

print(isinstance([1,2,3],(list,tuple)))
print(isinstance((1,2,3),(list,tuple)))

print(dir('ABC'))
print(len('ABC'))
print('ABC'.__len__())

class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))

print('ABC'.lower())

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj,'x'))
print(obj.x)
print(hasattr(obj,'y'))

setattr(obj,'y',19)
print(hasattr(obj,'y'))
print(getattr(obj,'y'))
print(obj.y)

#print(getattr(obj,'z'))
print(getattr(obj,'z',404))

print(hasattr(obj,'power'))
print(getattr(obj,'power'))

fn = getattr(obj,'power')
print(fn)
print(fn())

class Student(object):
    def __init__(self,name):
        self.name = name
s = Student('tsing')
s.score = 90






