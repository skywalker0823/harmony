# 此端負責所有短網址輸入與轉址服務

from crypt import methods
from flask import Blueprint, jsonify, request, redirect
import redis, string, random
short = Blueprint('short',__name__,template_folder="templates")
r = redis.Redis(host='redis', port=6379, db=0 , charset="utf-8" , decode_responses=True)


#接收到短網址轉址請求
@short.route("/<variable>",methods=["GET"])
def shorted(variable):
    print("=_=a",variable)
    #查詢並轉址
    # shorted_url = request.args.get("XD")
    # Redis check shorted if hit
    

    url = r.get(variable)
    if url == None:
        print("short url wrong!")
        return {"error":"Wrong shorted url"}
    else:
        return redirect(url,code=302)