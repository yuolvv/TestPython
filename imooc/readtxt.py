#!/usr/bin/env python
# encoding: utf-8

"""
@version: 2016
@author: yuolvv
@license: Apache Licence 
@file: readtxt.py
@time: 2016/10/5 8:36
"""

from urllib.request import urlopen

html = urlopen("https://en.wikipedia.org/robots.txt")

print(html.read().decode("utf-8"))