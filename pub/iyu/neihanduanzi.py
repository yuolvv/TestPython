#!/usr/bin/env python
# encoding: utf-8

"""
@version: 2016
@author: yuolvv
@license: Apache Licence 
@file: neihanduanzi.py
@time: 2016/10/5 9:21
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql.cursors

#请求URL并把结果用UTF-8编码
resp = urlopen("http://neihanshequ.com/").read().decode("utf-8")

#使用BeautifulSoup解析
soup = BeautifulSoup(resp,"html.parser")

#print(soup)
#print(soup.find_all("h1"))
#print(soup.find_all(attrs={"class": "title"}))
#print(soup.find_all(class_="title"))

duanzi = soup.find_all(class_="title")

count = 1

for dz in duanzi:

    if dz.get_text().find("登录") == -1 & dz.get_text().find("举报") == -1 & dz.get_text().find("投稿") == -1:
        print(str(count) + dz.get_text())
        count = count+1

        # 获取数据库链接
        connection = pymysql.connect(host='localhost',user='root',password='123456',db='duanzi',charset='utf8mb4')
        try:
            # 获取会话指针
            with connection.cursor() as cursor:
                # 创建sql语句
                sql = "insert into `duanzi`(`text`) VALUES(%s)"

                # 执行sql语句
                cursor.execute(sql, (dz.get_text()))

                # 提交
                connection.commit()
        finally:
            connection.close()