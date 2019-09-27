import requests
from bs4 import BeautifulSoup
import time
import random

#使用代理
link = "http://www.santostang.com/"
proxies = {'http': 'http://xxx.xxx.xxx.xxx:xxxx'}
response = requests.get(link, proxies=proxies)





link = "http://www.santostang.com/"

def scrap(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    r = requests.get(link, headers=headers)
    html = r.text
    soup = BeautifulSoup(html, "lxml")
    return soup

soup = scrap(link)
title_list = soup.find_all("h1", class_="post-title")
for eachone in title_list:
    url = eachone.a['href']
    print('开始爬取这篇博客：', url)
    soup_article = scrap(url)
    title = soup_article.find("h1", class_="view-title").text.strip()
    print('这篇博客的标题为:', title)
    sleep_time = random.randint(0, 2) + random.random() #间隔0-3秒
    print('开始休息：', sleep_time, '秒')
    time.sleep(sleep_time)

