import pymysql
import os, traceback
from dbutils.pooled_db import PooledDB
from dotenv import load_dotenv

load_dotenv()

POOL = PooledDB(
    creator=pymysql,
    maxconnections=7,
    mincached=3,
    blocking=True,
    ping=0,
    host="0.0.0.0",
    port=3306,
    user='root',
    password=os.getenv("DB_PASS"),
    database='harmony',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)

connection = POOL.connection()

class urls:
    def get_url():
        pass