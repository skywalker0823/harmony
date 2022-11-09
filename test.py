import redis, string, random
import urllib.request
from urllib.request import Request, urlopen
from urllib.parse import urlparse

number_of_strings = 5
length_of_string = 8

r = redis.Redis(host='127.0.0.1', port=6379, db=0 , charset="utf-8" , decode_responses=True)


url_here = "https://www.msn.com/zh-tw/news/living/%E4%BB%8A%E5%9F%BA%E5%AE%9C%E7%9F%AD%E6%9A%AB%E9%9B%A8%E5%8C%97%E9%83%A8%E9%99%BD%E5%85%89%E9%9C%B2%E8%87%89-%E6%98%8E%E5%BE%8C%E5%A4%A9%E6%B0%B4%E6%B0%A3%E5%8F%88%E5%A2%9E%E5%A4%9A/ar-AA13SY69?ocid=msedgntp&cvid=05bfa30f76434639b2234f262904986c"


url_here = str(url_here)


if not urlparse(url_here).scheme:
        url_here = 'https://' + url_here
        req = Request(url_here, headers={'User-Agent': 'Mozilla/5.0'})


checker = urllib.request.urlopen(url_here).getcode()


print(checker)


if checker == 200:
    print("success")
    hit_check = r.get(url_here)
    print(hit_check,type(hit_check))
    if hit_check == None:
        # 資料樣態 長網址(一般網址):短網址(shorted)
        # 產出隨機hashed-shorted
        for x in range(number_of_strings):
            shorted_url = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
        r.set(url_here,shorted_url)
        r.set(shorted_url,url_here)
        print("ok_not_get")
        print(r.get(url_here))
    else:
        print("ok_get")
        print(r.get(url_here))
