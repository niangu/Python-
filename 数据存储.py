'''
#写数据，TXT
title = "This is a test sentence."
with open('/home/niangu/桌面/py爬虫/title.txt', "a+") as f:#   with open(r'/home/niangu/桌面/py爬虫/title.txt', "a+") as f:
    f.write(title)
    f.close()

output = '\t'.join(['name', 'title', 'age', 'gender'])
with open(r'/home/niangu/桌面/py爬虫/test.txt', "a+") as f:
    f.write(output)
    f.close()

#读取数据
with open('title.txt', "r", encoding='UTF-8') as f:
    result = f.read()
    print(result)

#读取test.csv
import csv
with open('test.csv', 'r', encoding='UTF-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)
        print(row[0])

#写入CSV
import csv
output_list = ['1', '2', '3', '4']
with open('test2.csv', 'a+', encoding='UTF-8', newline='') as csvfile:
    w = csv.writer(csvfile)
    w.writerow(output_list)
'''
'''
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='a112233.', db='scraping')
cur = conn.cursor()

cur.execute("INSERT INTO urls (url, content) VALUES ('www.baidu.com', 'This is content.')")
cur.close()
conn.commit()
conn.close()
'''
'''
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.blog_database
collection = db.blog
'''
import pymysql

conn= pymysql.connect(host='localhost', user='root', passwd='jjj', db ='baidumap', charset="utf8")
cur = conn.cursor()
sql = """CREATE TABLE city (
         id INT NOT NULL AUTO_INCREMENT,
         city VARCHAR(200) NOT NULL,
         park VARCHAR(200) NOT NULL,
         location_lat FLOAT,
         location_lng FLOAT,
         address VARCHAR(200),
         street_id VARCHAR(200),
         uid VARCHAR(200),
         created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
         PRIMARY KEY (id)
         );"""
cur.execute(sql)
cur.close()
conn.commit()
conn.close()