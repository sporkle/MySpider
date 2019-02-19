# !/usr/bin/env/python
# -*- coding:utf-8 -*-

import requests
from lxml import etree

url = 'https://weibo.com/5670473300'
html = requests.get(url)
code_out = html.apparent_encoding
html.encoding = code_out
print html.text