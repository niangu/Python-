import requests
from bs4 import BeautifulSoup
def get_movies():
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            'Host': 'movie.douban.com'
    }
    movie_list = []
    for i in range(0, 10):
        if i == 0:
            link = 'https://movie.douban.com/top250'
        if i > 1:
            link = 'https://movie.douban.com/top250?start=' + str(i * 25) + '&filter='
        r = requests.get(link, headers=headers, timeout=10)
        print(str(i* 25), "页面响应状态码：", r.status_code)

        soup = BeautifulSoup(r.text, 'lxml')
        div_list = soup.find_all('div', class_='hd')
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)
    return movie_list




movies = get_movies()
print(movies)



