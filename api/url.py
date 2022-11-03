from crypt import methods
from unittest import result
from flask import Blueprint, jsonify,request

url = Blueprint('url',__name__,template_folder="templates")

@url.route("/api/get_url",methods=["GET"])
def get_url(): 
    url_here = request.args.get("url_here")
    print(url_here)
    #先進資料庫查訊是否有該網址
    #有回傳hashed-shortend網址
    #無則新增 avoid collision.

    return {"ok":"This is get url_here"}