#process_youyuan_mysql.py

# -*- coding: utf-8 -*-

import json
import redis
import pymysql

def main():
    # 指定redis数据库信息
    rediscli = redis.StrictRedis(host='127.0.0.1', port = 6379, db = 8)
    # 指定mysql数据库
    mysqlcli = pymysql.connect(host='127.0.0.1', user='root', passwd='123123', db = 'test1', port=3306, use_unicode=True)

    while True:
        # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
        source, data = rediscli.blpop(["leo"])

        # try:
        item = json.loads(data.decode())
        # print("source=======", source)
        # print("item=========", item)
        # except Exception as e:
        #         print("类型错误", e)

        try:
            # 使用cursor()方法获取操作游标

            cur = mysqlcli.cursor()
            # 使用execute方法执行SQL INSERT语句
            cur.execute("INSERT INTO names(age) VALUES (%s)" [item['age']] )
            # 提交sql事务
            mysqlcli.commit()
            #关闭本次操作
            cur.close()
            # print("inserted %s" % item['source_url'])
        except pymysql.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

if __name__ == '__main__':
    main()