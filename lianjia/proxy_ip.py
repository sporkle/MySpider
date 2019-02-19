# _*_ conding:utf-8 _*_
import requests

proxies = {
   "http": "http://116.11.254.37:80",
   "https" : "https://42.202.130.246:3128"
}

url = 'https://cs.lianjia.com/ershoufang/pg99/'
r = requests.get(url, proxies = proxies)
print r