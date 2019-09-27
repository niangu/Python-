import requests
import json
import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='a112233.', db='baidumap', charset="utf8")
cur = conn.cursor()


def getjson(loc, page_num):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    pa = {
        'q': '公园',
        'region': loc,
        'scope': '2',
        'page_size': 20,
        'page_num': page_num,
        'output': 'json',
        'ak': 'DDtVK6HPruSSkqHRj5gTk0rc'
    }

    r = requests.get("http://api.map.baidu.com/place/v2/search", params=pa, headers=headers)
    decodejson = json.loads(r.text)
    return decodejson
city_list = list()
with open("cities.txt", 'r', encoding='utf-8') as txt_file:
    for eachLine in txt_file:
        if eachLine != "" and eachLine != "\n":
            fields = eachLine.split("\t")
            city = fields[0]
            city_list.append(city)
    txt_file.close()

for eachcity in city_list:
    not_last_page = True
    page_num = 0
    while not_last_page:
        decodejson = getjson(eachcity, page_num)
        print(eachcity, page_num)
        if decodejson['results']:
            for eachone in decodejson['results']:
                try:
                    park = eachone['name']
                except:
                    park = None
                try:
                    location_lat = eachone['location']['lat']
                except:
                    location_lat = None
                try:
                    location_lng = eachone['location']['lng']
                except:
                    location_lng = None
                try:
                    address = eachone['address']
                except:
                    address = None
                try:
                    street_id = eachone['street_id']
                except:
                    street_id = None
                try:
                    uid = eachone['uid']
                except:
                    uid = None
                sql = """INSERT INTO baidumap.city
                (city, park, location_lat, location_lng, address, street_id, uid)
                VALUES
                (%s, %s, %s, %s, %s, %s, %s);"""

                cur.execute(sql, (eachcity, park, location_lat, location_lng, address, street_id, uid,))
                conn.commit()
            page_num += 1
        else:
            not_last_page = False
cur.close()
conn.close()