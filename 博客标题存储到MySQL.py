import requests
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='jjjjj', db='scraping', charset="utf8")
cur = conn.cursor()

link = "http://www.santostang.com/"
headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
r = requests.get(link, headers=headers)

soup = BeautifulSoup(r.text, "lxml")
title_list = soup.find_all("h1", class_="post-title")
for eachone in title_list:
    url = eachone.a['href']
    title = eachone.a.text.strip()

    cur.execute("insert into urls (url, content) values (%s, %s)", (url, title))

cur.close()
conn.commit()
conn.close()
