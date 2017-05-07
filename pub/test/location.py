#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0.0
@author: yuolvv
@license: Apache Licence 
@file: location.py
@time: 2016/10/26 14:01
"""

import re
import urllib.request
import json

def get_ip():
    url = 'http://ip.chinaz.com/getip.aspx'
    opener = urllib.request.urlopen(url)
    str = opener.read()
    str = str.decode("utf8")
    ip = re.search('\d+\.\d+\.\d+\.\d+',str).group(0)
    print("\n当前位置IP：" + ip)
    return ip

def get_ip_information(ip):
    url='http://api.map.baidu.com/highacciploc/v1?qcip='+ip+'&qterm=pc&ak=y1HgU7An49qyP0i9GnIgvTxzmND58X0Y&coord=bd09ll&extensions=3'
    poiss=''
    request = urllib.request.Request(url)
    page = urllib.request.urlopen(request,timeout=10)
    data_json = page.read()
    #print(data_json)
    data_dic = json.loads(data_json.decode("utf8"))
    if "content" in data_dic:
        content = data_dic["content"]
        address_component = content["address_component"]
        formatted_address = content["formatted_address"]
        print("\n该IP地址的具体位置为："+address_component["country"]+formatted_address)

        if "pois" in content:
            print("\n该IP地址附近POI信息如下：")
            pois = content["pois"]
            for index in range(len(pois)):
                pois_name = pois[index]["name"]
                pois_address = pois[index]["address"]
                pois_tag = pois[index]["tag"]
                print(pois_name+"----"+pois_address+"----"+pois_tag)
    else:
        print("IP地位失败！")

getip = get_ip()

#get_ip_information('116.25.162.64')
get_ip_information(getip)