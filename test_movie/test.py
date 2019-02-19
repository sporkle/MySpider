# coding = utf-8
import requests

url = 'http://www.ygdy8.net/html/gndy/dyzz/20170819/54765.html'
html = requests.get(url)
# 文件编码的转换
code_out = html.apparent_encoding
html.encoding = code_out

print html.text
