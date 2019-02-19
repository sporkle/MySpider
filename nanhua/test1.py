# !/usr/bin/env python
# -*- coding:utf-8 -*-
import requests


def login():
    session = requests.session()
    # res = session.get('http://my.its.csu.edu.cn/').content

    login_data = {
        'userName': '3903150327',
        'passWord': '136510',
        'enter': 'true'
    }
    session.post('http://my.its.csu.edu.cn//', data=login_data)
    res = session.get('http://my.its.csu.edu.cn/Home/Default')
    print(res.text)


login()
