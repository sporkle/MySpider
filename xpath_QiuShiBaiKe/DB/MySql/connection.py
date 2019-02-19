# ! /usr/bin/env python
# -*- coding:utf-8 -*-

import MySQLdb
db = MySQLdb.connect("localhost","root","123456","scrapy")

cursor = db.cursor()

sql = """insert into conntection(num,name) VALUES (2,'xiang')"""


cursor.execute(sql)
db.commit()
print "ok"


db.close()