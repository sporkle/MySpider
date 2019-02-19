# _*_ coding:utf-8 _*_
import re
from lxml import etree
import requests
from multiprocessing import Pool
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def getHtml(url):
    html = requests.get(url)
    code_out = html.apparent_encoding
    html.encoding = code_out
    print url
    return html.text

def getTitle_author(html):
    source = etree.HTML(html)
    items = source.xpath('//tr[@class="tr3"]')
    messages = {}
    Titles = []
    Authors = []
    for item in items:
        need = item.xpath('td[@class="subject"]')
        page_title = item.xpath('td[@class="subject"]/a[1]//text()')
        page_author = item.xpath('td[@class="author"]/a[1]/text()')
        page_time = item.xpath('td[@class="author"]/p[1]/text()')
        if need:
            title = 'Title: '+ str(page_title[0])
            Titles.append(title)
            author = 'Author: ' + str(page_author[0]) + '   ' + str(page_time[0])
            Authors.append(author)
    messages['title'] = Titles
    messages['author'] = Authors
    return messages

def getUrl(html):
    source = etree.HTML(html)
    items = source.xpath('//tr[@class="tr3"]')
    content = []
    for item in items:
        need = item.xpath('td[@class="subject"]')
        page_url = item.xpath('td[@class="subject"]/a[1]/@href')
        if need:
            # print page_url[0]    test
            content.append(page_url[0])
        # print 'Done'
    return content

def makeUrl(content):
    url1 = 'https://bbs.2cto.com/'
    article_urls = []
    for each in content:
        url = url1 + each
        article_urls.append(url)
        # print url
    return article_urls

def showMessage (titles,authors,urls):
    for title,author,url in zip(titles,authors,urls):
        print title,author + '\n' + url

class getArticContent:
    def __init__(self):
        print 'get content now.'
        self.replace = replace()


    def getHtml(self,url):
        html = requests.get(url)
        code_out = html.apparent_encoding
        html.encoding = code_out
        return html.text

    def getTitle(self,html):
        pattern = 'class="read_h1">(.*?)<a href="javascript:;'
        title = re.search(pattern, html, re.S).group(1)
        # print title    test
        return title

    def getContent(self,html):
        pattern = 'id="read_tpc">(.*?)</div>'
        content = re.search(pattern, html, re.S).group(1)
        finall_content = self.replace.replace(content)
        # print  finall_content
        return finall_content

class replace:
    def replace(self,x):
        replaceNextLine = re.compile('</font></font>')
        replaceNextLine_1 = re.compile('<br />')
        replaceAddr = re.compile('<.*?>')
        replaceQuote = re.compile('&#39')
        replaceSpac = re.compile('&nbsp')
        replaceCont = re.compile(';')
        x = re.sub(replaceNextLine_1, "\n", x)
        x = re.sub(replaceNextLine, "\n", x)
        x = re.sub(replaceAddr, "", x)
        x = re.sub(replaceQuote, "\'", x)
        x = re.sub(replaceSpac, "", x)
        x = re.sub(replaceCont, "", x)
        return x

def saveMessage(titles,authors,urls):
    print "begine write this url catalog"
    fp = open("E:\python_dataCatch\catch_web\honghei\content" + "\honghei.txt",'a')
    for title,author,url in zip(titles,authors,urls):
        lines = title + '    ' + author + '\n' + url + '\n\n'
        fp.write(lines)
    fp.close()
    print 'write catalog Done!'

def saveArtics(titles,contents,page_num):
    fp = open("E:\python_dataCatch\catch_web\honghei\content" + "\honghei_news_" + str(page_num)+ ".txt",'w')
    i = 0
    for title, content in zip(titles, contents):
        parting_lines = "-----------------------------------------------------------" + str(i) + "-----" \
                                                                                                 "------------------------------------------------------\n"
        artic = '0X' + str(i) + ': \n' + '     ' + title + '\n' + content + '\n\n\n\n'
        fp.write(parting_lines)
        fp.write(artic)
        i += 1
    fp.close()
    print 'write article done!'

base_url = 'https://bbs.2cto.com/thread.php?fid=33&page='

def start():
    for page_num in range(356,1001):
        url = base_url + str(page_num)
        print 'handing:' + url
        html = getHtml(url)
        page_urls = getUrl(html)
        article_urls = makeUrl(page_urls)
        messages = getTitle_author(html)
        titles = []
        authors = []
        for title,message in zip(messages['title'],messages['author']):
            # print title,message
            titles.append(title)
            authors.append(message)
        # showMessage(titles, authors, article_urls)
        saveMessage(titles, authors, article_urls)


        artic = getArticContent()
        article_titles = []
        article_content = []
        for each in article_urls:
            html = artic.getHtml(each)
            title = artic.getTitle(html)
            content = artic.getContent(html)
            article_titles.append(title)
            article_content.append(content)
        saveArtics(article_titles,article_content,page_num)

if __name__ == "__main__":
    pool = Pool(8)
    pool.apply_async(func= start)

    print ('start multiprocessing. 0.0')
    # if apply_async print this statument
    pool.close()
    pool.join()
    print ('end multiprocessing. +.+')
