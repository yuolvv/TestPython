#!/usr/bin/env python
# encoding: utf-8

"""
@version: 2016
@author: yuolvv
@license: Apache Licence 
@file: posttest.py
@time: 2016/9/25 11:05
"""

from urllib.request import urlopen
from urllib.request import Request
from urllib import parse

req = Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")
postData = parse.urlencode([
    ("StartStation","977abb69-413a-4ccf-a109-0272c24fd490"),
    ("EndStation","9c5ac6ca-ec89-48f8-aab0-41b738cb1814"),
    ("SearchDate","2016/09/25"),
    ("SearchTime","11:00"),
    ("SearchWay","DepartureInMandarin")
])

req.add_header("Origin", "http://www.thsrc.com.tw")
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36")
resp = urlopen(req, data=postData.encode("utf-8"))
print(resp.read().decode("utf-8"))











