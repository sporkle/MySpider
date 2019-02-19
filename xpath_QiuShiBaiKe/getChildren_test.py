# -*- coding:utf-8 -*-
from lxml import etree

html = """
<ul id="parameter2" class="p-parameter-list">
 <li title='养生堂天然维生素E软胶囊'>商品名称：养生堂天然维生素E软胶囊</li>
 <li title='720135'>商品编号：720135</li>
 <li title='养生堂'>品牌：<a>养生堂</a></li>
</ul>
"""

html = html.decode("utf-8")
tree = etree.HTML(html)

property_list_reg = '//ul[@id="parameter2"]/li'


def tryFindChild(element):
    children = element.getchildren()
    if len(children):
        return element.text + " " + children[0].text
    else:
        return element.text


property_lst = tree.xpath(property_list_reg)
for e in property_lst:
    print tryFindChild(e)

print len(property_lst)