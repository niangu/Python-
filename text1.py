import requests
from pymongo import MongoClient
import json
import time
import random

client = MongoClient('localhost', 27017)

db1 = client.admin
db1.authenticate("niangu", "ffff", mechanism='SCRAM-SHA-1')

db = client.zhihu_database
collection = db.live


def scrapy(link):
    headers = {
        'Host': 'api.zhihu.com',
        'Origin': 'https://www.zhihu.com',
        'Referer': 'https://www.zhihu.com/lives',
        'authorization': 'oauth 8274ffb553d511e6a7fdacbc328e205d',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
    }
    r = requests.get(link, headers=headers)
    return (r.text)


link = "https://api.zhihu.com/lives/homefeed?includes=live"
is_end = False
while not is_end:
    html = scrapy(link)
    decodejson = json.loads(html)
    collection.insert_one(decodejson)

    link = decodejson['paging']['next']
    is_end = decodejson['paging']['is_end']
    time.sleep(random.randint(2, 3) + random.random())