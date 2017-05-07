#!/usr/bin/env python
# encoding: utf-8

"""
@version: 2016
@author: yuolvv
@license: Apache Licence 
@file: GetPicture.py
@time: 2016/10/5 9:11
"""
import re
import urllib.request


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg' % x)
        x = x + 1


html = getHtml("http://tieba.baidu.com/p/2460150866")
getImg(html)