# _*_ coding:utf-8 _*_
import re
import urllib
import urllib2
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
headers = {'User-agent' : user_agent}

def replace(x):
    remove = re.compile('\n')
    chang = re.compile('<br/>')
    x = re.sub(remove,"",x)
    x = re.sub(chang,"\n",x)
    return x

for i in range(1,2):
    page = i
    url = 'https://www.qiushibaike.com/8hr/page/' + str(page) +'/'
    try:
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        pattern = re.compile('<div class="author clearfix">.*?<img src=.*? alt=(.*?)>.*?<div class="content">\n<span>(.*?)</span>'
                             + '.*?<!-- .*? -->(.*?)<div class="stats">',re.S)
        items = re.findall(pattern,content)
        for item in items:
            haveImg = re.search("img",item[2])
            if not haveImg:
                print item[0] + '\n' + replace(item[1]) +'\n\n'
        print "done!"
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason