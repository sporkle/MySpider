# ! /user/bin/env python
# -*- coding:utf-8 -*-
# author: leo_xiang
# time:   2017.10.30 17:27

import requests
import time
from lxml import etree


def get_articUrl (basic_url):
    '''
    : 找到每个文章的url
    : 将这个函数作为一个生成器函数
    :param basic_url: 得到搜索微信网站的原始URl（url格式可以构造）
    :return:
    '''
    html    = requests.get(basic_url)
    source  = etree.HTML(html.text)
    items   = source.xpath('//ul[@class="news-list"]/li')
    for item in items:

        artic_url = item.xpath('div[1]/a[1]/@href')
        if (artic_url):
            artic_url = artic_url
        else:
            artic_url = item.xpath('div[1]/h3/a[1]/@href')
        print artic_url[0]
        yield artic_url[0]
    time.sleep(2)


def getMessages(artic_url):
    html    = requests.get(artic_url)
    # print type(html.text)
    source  = etree.HTML(html.text)
    content = {}
    content['title']    = source.xpath('//*[@id="activity-name"]/text()')[0].strip()
    content['pub_time'] = source.xpath('//*[@id="post-date"]/text()')[0].strip()
    content['pub_name'] = source.xpath('//*[@id="post-user"]/text()')[0].strip()
    print content


def main():
    start_url   = 'http://weixin.sogou.com/weixin?query=%E7%89%A9%E8%81%94%E7%BD%91&type=2&page=1&ie=utf8'
    urls        = [url for url in get_articUrl(start_url)]
    for url in urls:
        getMessages(url)
    print "Done"


if __name__ == "__main__":
    main()