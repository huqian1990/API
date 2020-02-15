#-*-coding:utf-8-*-
#数据库封装方法#
import requests
import random
import unittest
from lib.db_conn import query_db,del_db,get_conn


# ====先输入查询信息
# id_card="321023199029388827"   #居民身份证
# resident_name="小小黄"       #居民姓名
# "buildId":    110 ,   #居民楼栋
# "tagIds": [19]   ,     #居民标签
# "isFocus":  "true"     #是否关注重点：true_是；false_否；不限就不传数据


#####查询数据库中存在的未删除的居民信息
conn=get_conn()
result=query_db(conn,"SELECT resident_id,resident_name,id_card FROM resident_info WHERE del_flag='0'")
info=random.choice(result)
resident_id=info[0]
resident_name=info[1]
id_card=info[2]




#查询居民详情列表:全部信息列表
class TestQuery(unittest.TestCase):
    def test_query_people_list(self):
        print("=============查询全部居民信息列表========")
        url = "http://47.103.35.164:5002/smart/baseresidentinfo/list"
        headers = {
            "userID": '1014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = {
            "pageNum": 1,
            "pageSize": 10
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.json())
        res_dict = res.json()
        res_code = res_dict['code']
        res_total = res_dict['total']
        res_message = res_dict['message']
        print("查询居民列表_返回码:{},{}".format(res_code, res_message))
        print("查询居民列表共有'{}'条数据".format(res_total))




# ========查询居民详情列表——条件查询：身份证/姓名/楼栋/关注重点等等=========
    def test_query_people_list_idcard(self):
        print("=============根据姓名或者身份证查询居民信息列表========")
        url = "http://47.103.35.164:5002/smart/baseresidentinfo/list"
        headers = {
            "userID": '1014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data={
            "pageNum": 1,
            "pageSize": 10,
            "keyword": id_card,    #身份证号
            # "keyword": resident_name,     #居民姓名
            # "buildId":    110 ,   #居民楼栋
            # "tagIds": [19]   ,     #居民标签
            # "isFocus":  "true"     #是否关注重点：true_是；false_否；不限就不传数据
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.json())
        res_dict = res.json()
        res_code = res_dict['code']
        res_total = res_dict['total']
        res_message = res_dict['message']
        print("查询居民列表_返回码:{},{}".format(res_code, res_message))
        print("查询居民列表共有'{}'条数据".format(res_total))


if __name__=="__main__":
    unittest.main()








