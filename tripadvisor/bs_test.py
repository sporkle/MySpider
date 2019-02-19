# _*_ coding:utf-8 _*_
from bs4 import BeautifulSoup
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


headers = {
    'User_agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Cookie' : 'fr=0deyvLcvJybKIy9gl..BZq7ao...1.0.BZq7ao.'
}
def replace(x):
    remove = re.compile('\n')
    x = re.sub(remove,"",x)
    return x

def showInfo(url):
    print "handing url: " + url
    html = requests.get(url,headers=headers)
    soup = BeautifulSoup(html.text,'lxml')
    titles = soup.select('div.listing_title > a')
    nums = soup.select('div.listing_rating > div:nth-of-type(3)')
    scores = soup.select('div.listing_rating > div:nth-of-type(2) > div > span:nth-of-type(1)')

    info = []
    for title,num,score in zip(titles,nums,scores):
        data = {
            'title': title.get_text(),
            'num'  : num.get_text(),
            'score': score.get('alt'),
        }
        info.append(data)

    # f = open("changsha_tripAdivors00.txt",'a')
    for each in info:
        print "Title: " + each['title'] + "\nnums: " + replace(each['num']) + "\nscore: " + each['score'] + '\n\n'
        # f.writelines("Title: " + each['title'] + "\nnums: " + replace(each['num']) + "\nscore: " + each['score'] + '\n\n')

    # f.close()



# base_url = 'https://cn.tripadvisor.com/Attractions-g60763-Activities-oa00-New_York_City_New_York.html'
# url_1 = 'https://cn.tripadvisor.com/Attractions-g60763-Activities-oa'
# url_2 = '-New_York_City_New_York.html'
#
# showInfo(base_url)
#
# for page_num in range(630,930,30):
#     url = url_1 + str(page_num) + url_2
#     showInfo(url)

# 衡阳景点
# HY_url = 'https://cn.tripadvisor.com/Attractions-g679670-Activities-Hengyang_Hunan.html'
# showInfo(HY_url)

# changsha
cs_url = 'https://cn.tripadvisor.com/Attractions-g494932-Activities-Changsha_Hunan.html'
url_1 = 'https://cn.tripadvisor.com/Attractions-g494932-Activities-oa'
url_2 = '-Hengyang_Hunan.html'

# showInfo(cs_url)

for page_num in range(60,90,30):
    url = url_1 + str(page_num) + url_2
    showInfo(url)