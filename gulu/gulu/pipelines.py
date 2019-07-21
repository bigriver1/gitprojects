# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import pymysql
from datetime import datetime

class GuluPipeline(object):
    def process_item(self, item, spider):
        #utcnow() 是获取UTC时间
        item["crawled"] = datetime.utcnow()
        # 爬虫名
        item["spider"] = spider.name
        return item
# from twisted.enterprise import adbapi
# import pymysql
# import json
# from scrapy.crawler import Settings as settings
#
# class GuluPipeline(object):
#
#     def __init__(self):
#         self.connect = pymysql.connect(host='127.0.0.1',
#                                    user='root',
#                                    passwd='123123',
#                                    db='test1',
#                                    port=3306,
#                                    use_unicode=True)
#
#         # 通过cursor执行增删查改
#         self.cursor = self.connect.cursor();
#
#     def process_item(self, item, spider):
#
#             try:
#                 # 插入数据
#
#                 self.cursor.execute(
#                     'insert into guruin_list(url, title, content, imgae_url ) value (%s, %s, %s, %s)',
#                     (dict(item['url']), dict(item['title']), dict(item['content']), dict(item['image_url']),))
#
#                 # 提交sql语句
#                 self.connect.commit()
#
#             except Exception as error:
#                 # 出现错误时打印错误日志
#                 print(error)
#             return item

    '''
    The default pipeline invoke function
   
        def process_item(self, item,spider):
            res = self.dbpool.runInteraction(self.insert_into_table,item)
                return item

        def insert_into_table(self,conn,item):
                conn.execute('insert into zreading(title,author,pub_date,types,tags,view_counts,content) values(%s,%s,%s,%s,%s,%s,%s)', (item['title'],item['author'],item['pub_date'],item['types'],item['tags'],item['view_count'],item['content']))
    
    '''