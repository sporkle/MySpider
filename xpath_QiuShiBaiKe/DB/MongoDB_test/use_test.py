# _*_coding:utf-8_*_
import requests
from lxml import etree
import pymongo
import multiprocessing.dummy
from multiprocessing import Lock
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# connect mongoDB
connection = pymongo.MongoClient()
dba = connection.honghei_test0
post_info = dba.really


def getHtml(url):
    html = requests.get(url)
    code_out = html.apparent_encoding
    html.encoding = code_out
    return html.text

def getMessage(html):
    content = etree.HTML(html)
    everyMessage = content.xpath('//tr[@class="tr3"]')

    messages = []
    for each in everyMessage:
        message = {}
        judge = each.xpath('td[@class="subject"]/a[1]/@href')
        # page_title = item.xpath('td[@class="subject"]/a[1]//text()')
        # page_author = item.xpath('td[@class="author"]/a[1]/text()')
        # page_time = item.xpath('td[@class="author"]/p[1]/text()')
        # page_url = item.xpath('td[@class="subject"]/a[1]/@href')
        if judge:
            message['time'] = each.xpath('td[@class="author"]/p[1]/text()')[0]
            # print message['title']
            message['url'] = 'https://bbs.2cto.com/' + judge[0]
            message['author'] = each.xpath('td[@class="author"]/a[1]/text()')[0]
            message['title'] = each.xpath('td[@class="subject"]/a[1]//text()')[0]
            # print message
            # if "_id" in message:
            #     # print("_id in result_dict")
            #     del message["_id"]
            # post_info.insert(message)
            messages.append(message)
    # print "write Done!"
    return messages


lock = Lock()
def test(url):
    html = getHtml(url)
    messages = getMessage(html)
    for each in messages:
        if "_id" in each:
            # print("_id in result_dict")
            del each["_id"]
        lock.acquire()
        post_info.insert(each)
        lock.release()
    print "write Done"

if __name__ == "__main__":
    base_url = 'https://bbs.2cto.com/thread.php?fid=33&page='
    urls = []
    # html = getHtml(test_url)
    # # getMessage(html)
    # messages = getMessage(html)
    for num in range(1,1001):
        url = base_url + str(num)
        urls.append(url)

    pool = multiprocessing.dummy.Pool(8)
    results = pool.map(test,urls)
    pool.close()
    pool.join()