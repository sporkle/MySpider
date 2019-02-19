# -*-coding:utf-8 -*-
import  requests


proxies = {
   "http": "http://116.11.254.37:80",
   "https" : "https://42.202.130.246:3128"
}

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

url = 'https://cs.lianjia.com/ershoufang/pg1/'
r = requests.get(url , headers = headers)
print r.text