# -*- coding:utf-8 -*-
from lxml import etree
import requests
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

base_url = 'https://www.luogu.org/discuss/lists?forumname='

def getName(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    content = selector.xpath('//div[@class="am-g lg-table-bg0 lg-table-row"]')
    for each in content:
        names = each.xpath('div[1]/div[2]/span[1]/a/text()')
        for name in names:
            print name.encode("utf-8")
            file_put = open("test0.txt",'a')
            file_put.writelines(name + '\n')
            file_put.close()
    print 'Done!'

getName(base_url)