#!/usr/bin/env python
# encoding: utf-8

"""
@version: 2016
@author: yuolvv
@license: Apache Licence 
@file: urllibtest.py
@time: 2016/9/25 10:48
"""
from urllib import request

#resp = request.urlopen("http://www.baidu.com")
#print(resp.read().decode("utf-8"))

req = request.Request("http://www.baidu.com")
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36")
resp = request.urlopen(req)
print(resp.read().decode("utf-8"))
