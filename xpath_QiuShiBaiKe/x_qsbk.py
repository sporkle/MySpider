# _*_ coding:utf-8 _*_
import re
import requests
from bs4 import BeautifulSoup
from lxml import etree
import time
from pyquery import PyQuery as Q
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class spider:
    def __init__(self):
        print "spider begin:\n"
        self.i = 0
        self.child_text = ""


    # replace \n & <br> in content
    def replace(self,x):
        # replace_nextline = re.compile('\n')
        replace_space = re.compile('<br>')
        # x = re.sub(replace_nextline," ",x)
        # x = re.sub(replace_space,"\n",x)
        return x

    def getEveryClass(self,url):
        html = requests.get(url)
        print html.status_code
        page_file = etree.HTML(html.text)
        big_info = page_file.xpath('//*[@id="content-left"]/div')
        return big_info

    # get message from page
    def getInfo(self,big_info):
        # html = requests.get(url)
        # print html.status_code
        # page_file = etree.HTML(html.text)
        # big_info = page_file.xpath('//*[@id="content-left"]/div')
        names = []
        # for each in big_info:
        info = {}
        info['name']= big_info.xpath('div[1]/a[2]/h2/text()')
        content = big_info.xpath('a[1]/div/span[1]/text()')
        contents = []
        print len(content)
        # print type(len(info['content']))
        for i in range(0,len(content)):
            # print type(i)
            contents.append(self.replace(content[i]))
        info['content'] = contents
        # for author in info['name']:
        #     name = self.replace(author.encode("utf-8"))
        #     print name
        #     names.append(name)
        info['stats'] = big_info.xpath('div[@class="stats"]/span[1]/i/text()')
        # for each in info['stats']:
        #     print each

        return info

    def saveInfo(self,info):
        today = time.strftime("%Y-%m-%d")
        file_name = today + "QiuShi.txt"
        f = open(file_name,"w")
        for each in info:
            f.writelines(each + '\n')
        f.close()
        print "write " + file_name + " done!"

    def show(self,info):
        for each in info:
            # name = self.replace(each['name'].encode("utf-8"))
            print each + '\n'

if __name__ == '__main__':
    baseUrl = 'https://www.qiushibaike.com/8hr/page/1/'
    everyClassinfo = []
    qsbk = spider()
    classInfo = qsbk.getEveryClass(baseUrl)
    for each in classInfo:
        info = qsbk.getInfo(each)
        print info['content'][0]
        # name = info['name']
        name = qsbk.replace(info['content'])
        # print qsbk.replace(name[0])
        everyClassinfo.append(name)
    qsbk.show(everyClassinfo)
