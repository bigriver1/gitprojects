#process_youyuan_mysql.py

# -*- coding: utf-8 -*-

import json
import redis
import pymysql


def main():

    # 指定redis数据库信息
    rediscli = redis.StrictRedis(host='127.0.0.1', port = 6379, db = 1)
    # 指定mysql数据库
    mysqlcli = pymysql.connect(host='127.0.0.1', user='root', passwd='123123', db = 'test1', port=3306, use_unicode=True)

    while True:
        # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
        source, data = rediscli.blpop(["gl:items"])

        # try:
        item = json.loads(data.decode())
        # 打印 source和item的数据
        print("source=======", source)
        print("item=========", item)
        # except Exception as e:
        #         print("类型错误", e)

        try:

            # 使用cursor()方法获取操作游标
            cur = mysqlcli.cursor()
            sql = "insert into car(title, content_text, image_url, detail_url, addtime, tag, type, update_time,detail_img) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s )"
            # 使用execute方法执行SQL INSERT语句
            cur.execute(sql, [item['title'], item['content_text'], item['image_url'], item['detail_url'], item['addtime'], item['tag'],item['type'], item['update_time'], item['detail_img']])
            # 提交sql事务
            mysqlcli.commit()

            # 关闭本次操作
            cur.close()
            # print("inserted %s" % item['source_url'])
        except pymysql.Error as e:
            # 打印错误内容
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
            # print("插入数据错误", e)

if __name__ == '__main__':
    main()