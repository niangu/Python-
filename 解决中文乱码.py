#encode #将Unicode编码转换成其他编码的字符串
#decode #将其他编码的字符串转换成Unicode编码
'''
import chardet #GBK

str1 = "我们"
str_utf8 = str1.encode('utf-8')
print(str_utf8)

str_decode = str1.encode('utf-8').decode('utf-8')

str_gbk = "我们".encode('gbk')
chardet.detect(str_gbk)

'''
'''
import requests
from bs4 import BeautifulSoup

url = 'http://w3shool.com.cn/'
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
r.encoding = 'gb2312'
xx = soup.find('div', id='w3').h2.text
print(xx)

str1 = '网站的非法字符即非一种字符'
str1.decode('GBK', 'ignore') #decode第二个参数：ignore, replace, xmlcharrefreplace

'''
import requests

url = 'http://www.sina.com.cn/'
r = requests.get(url)
#print(r.text)

import chardet
after_gzip = r.content
print('解压后字符串的编码为', chardet.detect(after_gzip))
print(after_gzip.decode('UTF-8'))

#打开文件时
result_ANSI = open('test_ANSI.txt', 'r', encoding='ANSI').read()
print(result_ANSI)
result_utf8 = open('test_utf8.txt', 'r', encoding='UTF-8').read()
print(result_utf8)

#保存文件
title = '我们'
with open('title.txt', 'a+', encoding='UTF-8') as f:
    f.write(title)
    f.close()

#保存JSON文件
import json
title = '我们love你们'
with open('title.json', 'w', encoding='UTF-8') as f:
    json.dump([title], f, ensure_ascii=False)





