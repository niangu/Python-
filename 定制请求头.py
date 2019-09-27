import requests
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/73.0.3683.86 Safari/537.36',
    'Host': 'www.santostang.com'
    }
r = requests.get('http://www.santostang.com/', headers=headers)
print("响应状态码:", r.status_code)