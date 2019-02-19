# -*- coding:utf-8 -*-
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

base_url = 'https://www.luogu.org'
indexURL = 'https://www.luogu.org/discuss/lists?forumname='

# html = requests.get(indexURL)

def saveInfo(name):
    f = open('name2.txt','a')
    for each in name:
        name = str(each)
        f.writelines(name + '\n')
    f.close()
    print 'Done!'

def getName(url):
    html = requests.get(url)
    name_url = re.findall('class="lg-fg-.*?>(.*?)</a>',html.text,re.S)
    saveInfo(name_url)
    # for name in name_url:
    #     print name

def getAllName():
    for i in range(1,807):
        url = 'https://www.luogu.org/discuss/lists?forumname=&page=' + str(i)
        getName(url)



# getName(indexURL)
getAllName()