#-*-coding:utf-8-*-
#数据库封装方法#
import json
import pymysql
from config import DB_API_TEST

def get_conn():
    conn=pymysql.connect(**DB_API_TEST)
    return conn

def query_db(conn,sql):
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    return result


def del_db(conn,sql):
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

if __name__=="__main__":
    conn=get_conn()
    # print(query_db(conn,"SELECT * from resident_info WHERE id_card='321021101429903200'"))
    # del_db(conn,"DELETE from resident_info WHERE id_card='111222';")
    # print(query_db(conn,"SELECT * from resident_info WHERE id_card='111222';"))
