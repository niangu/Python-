from pymongo import MongoClient
client = MongoClient('localhost', 27017)

db = client.admin
db.authenticate("niangu", "sssss", mechanism='SCRAM-SHA-1')

db = client.zhihu_database
collection = db.live

first_page = collection.find_one()
for each in first_page['data']:
    print (each['live']['id'])