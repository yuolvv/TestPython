#!/usr/bin/env python
# encoding: utf-8

"""
@version: 2016
@author: yuolvv
@license: Apache Licence 
@file: readmysql.py
@time: 2016/10/5 8:25
"""

import pymysql.cursors

#获取数据库链接
connection = pymysql.connect(host='localhost',
                user='root',password='123456',
                db='wikiurl',charset='utf8mb4')

try:
    #获取会话指针
    with connection.cursor() as cursor:
        #查询语句
        sql = "select `urlname`,`urlref` from `urls` where `id` is not null"
        count = cursor.execute(sql)
        print(count)

        #查询数据
        #result = cursor.fetchall()
        result = cursor.fetchmany(size=2)
        print(result)

finally:
    connection.close()









































