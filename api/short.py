# 此端負責所有短網址輸入與轉址服務

from crypt import methods
from flask import Blueprint, jsonify, request

short = Blueprint('short',__name__,template_folder="templates")


#備用
@short.route("/xxx",methods=["GET"])
def shorted():
    #查詢並轉址
    shorted_url = request.args.get("XD")
    # Redis check shorted if hit
    


    return