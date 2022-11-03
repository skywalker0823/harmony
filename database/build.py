import pymysql
import os
from dotenv import load_dotenv

#docker run --name=a_mysql --platform linux/x86_64 -dp 3306:3306 -e MYSQL_ROOT_PASSWORD="" mysql:5.7

#Build main database
def build_database(conn):
    cursor.execute("DROP DATABASE IF EXISTS harmony")
    cursor.execute("CREATE DATABASE harmony")
    cursor.execute("USE harmony")
    conn.commit()

#Build main url table
def build_member(conn):
    cursor.execute("DROP TABLE IF EXISTS urls")
    sql = """CREATE TABLE urls(
        url_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        the_url varchar(255) NOT NULL
    )"""
    cursor.execute(sql)
    conn.commit()

if __name__ == "__main__":
    load_dotenv()
    conn = pymysql.connect(charset='utf8', host="0.0.0.0",
                           password=os.getenv("DB_PASS"), port=3306, user='eddie')
    cursor = conn.cursor()
    build_database(conn)
    build_member(conn)
    cursor.close()
    conn.close()