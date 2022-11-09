# 此端負責主要縮網址 api 服務

from flask import Blueprint, jsonify, request

import redis, string, random
import urllib.request
from urllib.request import Request, urlopen
from urllib.parse import urlparse
url = Blueprint('url',__name__,template_folder="templates")
r = redis.Redis(host='redis', port=6379, db=0 , charset="utf-8" , decode_responses=True)

#docker run --name a_redis -p 6379:6379 -d redis

# random generator settings
number_of_strings = 5
length_of_string = 8

@url.route("/api/get_url",methods=["GET"])
def get_url(): 
    url_here = request.args.get("url_here")
    url_here = str(url_here)
    print(">>>>>>>",url_here)
    #首先檢查輸入是否為合法/可用地址
    try:
        if not urlparse(url_here).scheme:
            url_here = 'https://' + url_here
        req = Request(url_here, headers={'User-Agent': 'Mozilla/5.0'})
        checker = urllib.request.urlopen(req).getcode()
        print(checker)
        if checker == 200:
            pass
        else:
            return {"error":"error"}
    except Exception as e:
            print(e)
            return {"error":"error_Except"}

    #這裡是使用者輸入的長網址
    print(url_here)

    hit_check = r.get(url_here)
    print(hit_check,type(hit_check))
    if hit_check == None:
        # 資料樣態 長網址(一般網址):短網址(shorted)
        # 產出隨機hashed-shorted
        for x in range(number_of_strings):
            shorted_url = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
        r.set(url_here,shorted_url)
        r.set(shorted_url,url_here)
        return {"ok_not_get":shorted_url}
    else:
        return {"ok_get":hit_check}


    #先進資料庫查訊是否有該網址
    #有回傳hashed-shortend網址
    #無則新增 avoid collision.

