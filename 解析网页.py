import re
m = re.match('www', 'www.santostang.com')
print("匹配的结果：", m)
print("匹配的起始与终点：", m.span())
print("匹配的起始位置:", m.start())
print("匹配的终点位置：", m.end())

line = "Fat cats smarter than dogs, is it right?"
m = re.match(r'(.*) are (.*?) dogs', line)
print('匹配的整句话', m.group(0))
print('匹配的第一个结果', m.group(1))
print('匹配的第二个结果', m.group(2))
print('匹配的结果列表', m.groups())


m_match = re.match('com', 'www.santostang.com')
m_search = re.search('com', 'www.santostang.com')
print(m_match)
print(m_search)

m_match = re.match('[0-9]+', '12345 is the first number, 23456 is the sencond')
m_search = re.search('[0-9]+', 'The first number is 12345, 23456 is the sencond')
m_findall = re.findall('[0-9]+', '12345 is the first number, 23456 is the sencond')
print(m_match.group())
print(m_search.group())
print(m_findall)


import requests
from bs4 import BeautifulSoup

link = "http://www.santostang.com/"
headers = {
    'User-Agent': ''
}
r = requests.get(link, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")
first_title = soup.find("h1", class_="post-title").a.text.strip()
print("第一篇文章的标题是：", first_title)

title_list = soup.find_all("h1", class_="post-title")
for i in range(len(title_list)):
    title = title_list[i].a.text.strip()
    print('第%s篇文章的标题是: %s' % (i+1, title))


html = 'abc'
soup = BeautifulSoup(html, "html.parser")
print(soup.prettify)

soup.header.h3#获取h3标签
soup.header.div.contents #用contents把它的子节点以列表的方式输出

for child in soup.header.div.children: #用children的方法获取所有子节点
    print(child)

for child in soup.header.div.descendants:
    print(child)

a_tag = soup.header.div.a
a_tag.parent #获取父节点的内容

soup.select("header h3")#通过tag标签逐层查找

#通过某个tag标签下的直接子标签遍历
print(soup.select("header > h3"))
print(soup.select("div > a"))

