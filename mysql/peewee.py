#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2015-03-12
'''''
pyspider结果保存到数据库简单样例,用peewee代替MySQLdb实现数据库操作.
使用方法：
    1, 把本文件放到pyspider/pyspider/database/mysql/目录下命名为mysqldb.py;
    2, 建立相应的表和库;
    3, 在脚本文件里使用from pyspider.database.mysql.mysqldb import ToMysql引用本代码;
    4, 重写on_result方法.
'''
from peewee import *

mysql_db = MySQLDatabase(
    host='',
    port=3306,
    database='kugou',
    user="root",
    passwd="",
    charset='utf8'
)

# 定义基础模型类,指定要使用那个数据库
class BaseModel(Model):
    class Meta:
        database = mysql_db

# 指定字段(或者列)
class testModel(BaseModel):
    name = CharField(null=True, default='')
    artist = CharField(null=True, default='')

    class Meta:
        db_table = 'peewee_test'


class ToMysql():

    def __init__(self):
        tables = [testModel]
        # mysql_db.connect()
        mysql_db.create_tables(tables, safe=True)

    def insert_into_test(self, **data):
        model = testModel()
        for k, v in data.iteritems():
            print k, v
            setattr(model, k, v)
        model.save()
