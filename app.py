from flask import Flask, redirect, session, render_template as rt
from api.url import url

app = Flask(__name__)


app.register_blueprint(url)


@app.route("/")
def index():
    return rt("index.html")




if __name__=="__main__":
    app.run(host="0.0.0.0",port=3000,debug=True)