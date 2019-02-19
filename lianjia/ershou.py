# -*- coding:utf-8 -*-
import requests
from lxml import etree
import pymongo
import re
from multiprocessing.dummy import Pool
from multiprocessing import Lock
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

connection = pymongo.MongoClient()
dba = connection.lianjia
post_info = dba.hz_ershou

def proxy_ip():
    proxies = {
        "http": "http://116.11.254.37:80",
        "https": "https://42.202.130.246:3128"
    }
    return proxies

headers = {
        'Host': "cs.lianjia.com" ,
        'Connection' : "keep-alive" ,
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
        'Accept' : "itext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Accept-Encoding' : "gzip, deflate, br",
        'Accept-Language' : "zh-CN,zh;q=0.8",
        'Cookie': "lianjia_uuid=1a6b249d-f4cc-45f0-9be7-8021246a049f; UM_distinctid=15e8defa8b1299-04218a78af596f-58462"
                  "91c-144000-15e8defa8b229d; _jzqx=1.1505634219.1505703320.3.jzqsr=cs%2Elianjia%2Ecom|jzqct=/.jzqsr=ca"
                  "ptcha%2Elianjia%2Ecom|jzqct=/; select_city=430100; all-lj=fa25c352c963a53c37faa70f46a58187; _jzqckmp"
                  "=1; _smt_uid=59bdef86.235de9a1; CNZZDATA1255849590=1176036809-1505617944-https%253A%252F%252Fbj.lian"
                  "jia.com%252F%7C1505993859; CNZZDATA1254525948=1638802261-1505616114-https%253A%252F%252Fbj.lianjia.c"
                  "om%252F%7C1505992635; CNZZDATA1255633284=78798706-1505618893-https%253A%252F%252Fbj.lianjia.com%252F"
                  "%7C1505996284; CNZZDATA1255604082=1422503689-1505619129-https%253A%252F%252Fbj.lianjia.com%252F%7C15"
                  "05992672; _qzja=1.206681498.1505620023136.1505718304314.1505997552406.1505997552406.1505997568074.0."
                  "0.0.36.11; _qzjb=1.1505997552405.2.0.0.0; _qzjc=1; _qzjto=2.1.0; _jzqa=1.1405706515737467600.1505619"
                  "849.1505718305.1505997549.11; _jzqc=1; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1505619843,1505699487"
                  ",1505997547; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1505997569; _jzqb=1.2.10.1505997549.1; _ga=GA1"
                  ".2.1474896653.1505619861; _gid=GA1.2.2142314897.1505997558; lianjia_ssid=0ecfd38e-c17c-440b-a25e-5c9"
                  "c41ad8fab"
}


class Ershou:
    def __init__(self):
        print "dealing ershou."
        self.lock    = Lock()
        self.proxies = proxy_ip()
        self.headers = headers

# get main url below url  -- every area url  hope use it make mongoDB list         ----now it does not help
#     def deal_url(self, url):
#         base         = 'https://cs.lianjia.com/'
#         html         = requests.get(url, headers = self.headers)
#         lxml_html    = etree.HTML(html.text)
#         urls         = lxml_html.xpath("/html/body/div[3]/div[1]/dl[2]/dd/div[1]/div/a/@href")
#         complet_urls = []
#         for each in urls:
#             fax_url  = base + each
#             complet_urls.append(fax_url)
#         # print complet_urls
#         return complet_urls


# get a singal url's messages
    def getMessages(self,url):
        self.lock.acquire()
        html        = requests.get(url)
        self.lock.release()
        lxml_html   = etree.HTML(html.text)
        messages    = []
        contents    = lxml_html.xpath('//li[@class="clear"]')
        print "test"
        for each in contents:
            message = {}

            adress      = each.xpath('div[1]/div[2]/div//text()')
            # 得到房屋的总面积
            content     = adress[1].encode('utf8')
            pattern     = u'厅(.*?)平米'
            pattern     = pattern.encode('utf8')
            Area_num    = re.search(pattern, content, re.S).group(1)
            # 楼层描述
            flood       = each.xpath('div[1]/div[3]/div//text()')
            # 得到总价
            totleprice  = each.xpath('div[1]/div[6]/div[1]/span/text()')
            # 得到含有平均价格的文字表达式  用正则表达出来。
            avg_price   = each.xpath('div[1]/div[6]/div[2]/span/text()')[0]
            content1    = avg_price.encode('utf8')
            pattern1    = u'单价(.*?)元'
            pattern1    = pattern1.encode('utf8')

            message['image']        = each.xpath('a[1]/img[1]/@data-original')[0]
            message['url']          = each.xpath('a[1]/@href')[0]
            message['title']        = each.xpath('div[1]/div[1]/a/text()')[0]
            message['adress']       = adress[0] + adress[1]
            message['totleArea']    = re.search('(\d+.\d+)|(\d+)', Area_num, re.S).group(1)
            message['flood']        = flood[0] + flood[1]
            message['totlePrice']   = totleprice[0]
            message['avgPrice']     = re.search(pattern1, content1, re.S).group(1)
            messages.append(message)
        return messages


# get Totle page num
    def geturls(self,url):
        baseurl     = url + 'pg'
        # html        = requests.get(url,headers = self.headers)
        html = requests.get(url)
        lxml_html   = etree.HTML(html.text)
        TotlePage   = lxml_html.xpath('/html/body/div[4]/div[1]/div[7]/div[2]/div/@page-data')
        result      = re.findall("{\"totalPage\":(.*?),\"cur", TotlePage[0])[0]
        print result
        urls        = []
        for each in range(1,int(result)):

            pageurl = baseurl + str(each) + "/"
            urls.append(pageurl)
            print pageurl
        return urls

    def write_db(self,url):
        messages    = self.getMessages(url)
        for each in messages:
            if "_id" in each:
                # print("_id in result_dict")
                del each["_id"]
            post_info.insert(each)



lock = Lock()
if __name__ == "__main__":
    # 长沙的二手房信息
    # url         = 'https://cs.lianjia.com/ershoufang/'
    # 北京的二手房信息
    # url         = 'https://bj.lianjia.com/ershoufang/'
    # 深圳的二手房信息
    # url         = 'https://sz.lianjia.com/ershoufang/'
    # 成都的二手房信息
    # url         = 'https://cd.lianjia.com/ershoufang/'
    # 杭州的二手房信息
    url         = 'https://hz.lianjia.com/ershoufang/'
    test        = Ershou()
    totleUrls   = test.geturls(url)
    pool        = Pool(5)

    for page_url in totleUrls:
        pool.apply_async(func=test.write_db, args=(page_url,))
    pool.close()
    pool.join()


