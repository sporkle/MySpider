# -*-coding:utf-8-*-
import requests
import re
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def getMessages( url):
    html = requests.get(url)
    lxml_html = etree.HTML(html.text)
    messages = []
    contents = lxml_html.xpath('//li[@class="clear"]')
    print "test"
    for each in contents:
        message = {}
        adress = each.xpath('div[1]/div[2]/div//text()')
        message['adress'] = adress[0] + adress[1]

        content = adress[1].encode('utf8')

        pattern = u'厅(.*?)平米'
        pattern = pattern.encode('utf8')

        # 得到房屋的总面积
        Area_num = re.search(pattern , content , re.S).group(1)
        message['totleArea'] = re.search('(\d+.\d+)' , Area_num , re.S).group(1)
        print message['totleArea']


        avg_price = each.xpath('div[1]/div[6]/div[2]/span/text()')[0]
        content1 = avg_price.encode('utf8')

        # ' | 168.75'
        pattern1 = u'单价(.*?)元'
        pattern1 = pattern1.encode('utf8')
        message['avgPrice'] = re.search(pattern1, content1 , re.S).group(1)
        print message['avgPrice']
        messages.append(message)
    return messages



if __name__ == "__main__":
    url = 'https://cs.lianjia.com/ershoufang/pg1/'
    getMessages(url)

