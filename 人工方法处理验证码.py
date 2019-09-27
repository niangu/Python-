import requests
import re
import os
from PIL import Image


def get_si_code():
    #si_code是一个动态变化的参数
    index_url = 'http://www.santostang.com/wp-login.php?action=register'
    #获取注册时需要用到的si_code
    index_page = session.get(index_url, headers=headers)
    html = index_page.text
    pattern = r'type="text" name="(.*?)" id="ux_txt_captcha_challenge_field" style="display:block;"'
    #这里用re.search方法找到si_code
    si_code = re.search(pattern, html).group(1)
    return si_code

def get_captcha(si_code):
    captcha_url = "http://www.santostang.com/wp-admin/admin-ajax.php?captcha_code=45934"
    r = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到%s目录找到captcha.jpg手动输入'%os.path.abspath('captcha.jpg'))
    captcha = input("please input the captcha\n")
    return captcha

def register(account, email, si_code):
    post_url = 'http://www.santostang.com/wp-login.php?action=register'
    postdata = {
        'user_login': account,
        'user_email': email,
        'ux_txt_captcha_challenge_field': si_code,
        'redirtect_to': '',
    }
    #调用get_captcha函数获取验证码数字
    postdata["captcha"] = get_captcha(si_code)
    #提交POST请求，进行注册
    register_page = session.post(post_url, data=postdata, headers=headers)
    #若输出打印结果为200,则表示注册成功
    print(register_page.status_code)


if __name__ == '__main__':
    agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    headers = {
        "Host": "www.santostang.com",
        "Origin": "http://www.santostang.com",
        "Referer": "http://www.santostang.com/wp-login.php",
        'User-Agent': agent
    }
    session = requests.session()
    #获取我们需要的验证码匹配码
    si_code = get_si_code()
    #调用注册函数进行注册
    account = '18341432113'
    email = 'a12345@qq.com'
    register(account, email, si_code)
