# _*_coding:utf-8 _*_
import requests
import re

def replace(x):
    replaceNextLine = re.compile('</font></font>')
    replaceNextLine_1 = re.compile('<br />')
    replaceAddr = re.compile('<.*?>')
    replaceQuote = re.compile('&#39')
    replaceSpac = re.compile('&nbsp')
    replaceCont = re.compile(';')
    x = re.sub(replaceNextLine_1, "\n", x)
    x = re.sub(replaceNextLine,"\n",x)
    x = re.sub(replaceAddr, "", x)
    x= re.sub(replaceQuote, "\'", x)
    x = re.sub(replaceSpac, "",x)
    x = re.sub(replaceCont,"",x)
    return x

url = 'https://bbs.2cto.com/read.php?tid=377828&ds=1'

html = requests.get(url)
code_out = html.apparent_encoding
html.encoding = code_out
pattern = 'id="read_tpc">(.*?)</div>'
content = re.search(pattern,html.text,re.S).group(1)
print replace(content)