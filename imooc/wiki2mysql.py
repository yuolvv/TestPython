#!/usr/bin/env python
# encoding: utf-8

"""
@version: 2016
@author: yuolvv
@license: Apache Licence 
@file: wiki.py
@time: 2016/9/25 11:43
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql.cursors

#请求URL并把结果用UTF-8编码
resp = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")

#使用BeautifulSoup解析
soup = BeautifulSoup(resp,"html.parser")
#print(soup)

#获取所有以/wiki/开头的a标签的href属性
listUrls = soup.findAll("a",href=re.compile("^/wiki/"))
#print(listUrls)

for url in listUrls:

    #print(url)

    if not re.search("\.(jpg|JPG)$",url["href"]):
        print(url.get_text(),"<-->","https://en.wikipedia.org"+url["href"])

        #获取数据库链接
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='123456',
                                     db='wikiurl',
                                     charset='utf8mb4')
        try:
            #获取会话指针
            with connection.cursor() as cursor:
                #创建sql语句
                sql = "insert into `urls`(`urlname`,`urlref`) VALUES(%s,%s)"

                #执行sql语句
                cursor.execute(sql,(url.get_text(),"https://en.wikipedia.org"+url["href"]))

                #提交
                connection.commit()
        finally:
            connection.close()