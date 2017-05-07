#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0.0
@author: yuolvv
@license: Apache Licence 
@file: TestExtends.py
@time: 2016/10/31 14:34
"""

class Animal(object):
    def run(self):
        print("Animal is running...")

class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()

a = list()
b = Animal()
c = Dog()

print(isinstance(a,list))
print(isinstance(b,Dog))
print(isinstance(c,Dog))
print(isinstance(c,Animal))

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())

class Timer(object):
    def run(self):
        print('Start...')

run_twice(Timer())