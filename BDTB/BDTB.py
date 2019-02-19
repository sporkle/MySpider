# _*_coding:utf-8 _*_
import re
import urllib2
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# 处理页面标签类
class Tool:
    # 去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        # strip()将前后多余内容删除
        return x.strip()


class BDTB:
    def __init__(self):
        self.tool = Tool()
        self.defaultTitle = u'baidutianba'
        self.floor = 0

    def getSource(self,pagNum):
        url = 'https://tieba.baidu.com/p/5176659692?see_lz=1&pn=' + str(pagNum)
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            # print response.read()
            return response
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"connect baiduTieba fail",e.reason
                return None

    def getTitle(self):
        # url = 'https://tieba.baidu.com/p/3138733512?see_lz=2&pn=1'
        html = self.getSource(1)
        # print html.read()
        pattern = re.compile('<h3 class="core_title_txt pull-left text-overflow.*?>(.*?)</h3>',re.S)
        Title = re.search(pattern,html.read())
        if Title:
            print Title.group(1)   # a test
            return Title.group(1).strip()
            # .strip() removes all whitespace at the start and end, including spaces, tabs, newlines and carriage
            # returns.Leaving it in doesn't do any harm, and allows your program to deal with unexpected
            # extra whitespace inserted into the file.
        else:
            return None

    def getPagNum(self):
        html = self.getSource(1)
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span class="red">(.*?)</span>',re.S)
        pagNum = re.search(pattern,html.read())
        if pagNum:
            # print pagNum.group(1)
            return pagNum.group(1).strip()
        else:
            return None

    def getContent(self,source):
        pattern = re.compile('class="d_post_content j_d_post_content ">(.*?)</div>',re.S)
        contents = re.findall(pattern,source.read())
        # floor = 0
        items = []
        for content in contents:
            # print floor,u'floor----------------------------------------------------------------------' \
            #             u'---------------------------------------------------------------------------' \
            #             u'---------------------------------------------------------------------------'
            # print self.tool.replace(content)
            # floor += 1
            item = '\n' + self.tool.replace(content) + '\n'
            items.append(item.encode('utf-8'))
        return items

    def setFileTitle(self,title):
        if title is not None:
            fileName = unicode(title,'utf-8')
            self.file = open(fileName+ ".txt",'w+')
            # 使用先将中文用unicode编码 才可以写入文件名
            # self.file = open("test0.txt",'w+')
        else:
            self.file = open(self.defaultTitle + ".txt","w+")

    def writeData(self,contents):
        for item in contents:
            if 1:
                floorline = '\n' + str(self.floor) + 'floor-------------------------------------------------------------' \
                                                     '----------------------------------------------------------------------------------------------------------'
                self.file.write(floorline)
            self.file.write(item)
            self.floor += 1

    def start(self):
        totle_pageNum = self.getPagNum()
        title = self.getTitle()
        self.setFileTitle(title)
        try:
            print "tottle " + str(totle_pageNum) + " page"
            for i in range(1,int(totle_pageNum) + 1):
                print "write page " + str(i) + " now"
                page = self.getSource(i)
                contents = self.getContent(page)
                self.writeData(contents)
        except IOError,e:
            print "something wrong for: " + e.message
        finally:
            print "Done!"


dbtb = BDTB()
dbtb.start()
