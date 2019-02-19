# -*- coding:utf-8 -*-
import pymongo

connection = pymongo.MongoClient()
tdb = connection.test
post_info = tdb.jikexueyuan1

jike00 = {'name': 'steven', 'age': 23, 'sex': 'man'}
jike01 = {'name': u'ju', 'age': 12, 'sex': u'男', 'other': u'他会吃饭'}
jike02 = {'name': u'小子1', 'age': 32, 'sex': u'女', 'other': None}
jike03 = {'name': u'小子2', 'age': 56, 'sex': u'未知'}

tdb.jikexueyuan1.insert(jike00)
# post_info.insert(jike00)
# post_info.insert(jike01)
# post_info.insert(jike03)
print u'操作完成'