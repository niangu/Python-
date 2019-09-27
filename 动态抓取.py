import requests

link = ""
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
r = requests.get(link, headers=headers)
print(r.text)

import json
json_data = json.loads(r.text)
comment_list = json_data['data']['comments']

for eachone in comment_list:
    message = comment_list[eachone]['content']
    print(message)
