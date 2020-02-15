#-*-coding:utf-8-*-
#数据库封装方法#
import requests
import unittest
from lib.db_conn import get_conn,query_db,del_db
import random
###################删除居民信息##############
class Test_Del_PeopleInfo(unittest.TestCase):
    def test_del_PeopleInfo(self):
        print("随机删除已登记的居民信息")
        # 环境监察以及数据准备
        conn = get_conn()
        result = query_db(conn, "SELECT resident_id FROM resident_info WHERE del_flag=0 ")
        #随机选取居民删除
        resident_id = random.sample(result, 1)
        a=resident_id[0][0]
        b=[]
        b.append(a)
        print("即将删除的居民resident_id:".format(a))
        url = "http://47.103.35.164:5002/smart/baseresidentinfo/delete"
        headers = {
            "userID": '1014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data =str(b)
        print(data)
        res = requests.post(url=url, headers=headers, data=data)
        res_dict = res.json()
        res_code = res_dict['code']
        res_message = res_dict['message']
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)
        print("随机删除的居民Id为{}".format(a))


    def test_delPPLInfo(self):
        #查找出未删除的居民信息
        conn = get_conn()
        result = query_db(conn, "SELECT resident_id,resident_name,id_card FROM resident_info WHERE del_flag='0'")
        info = random.choice(result)
        resident_id = info[0]
        resident_name = info[1]
        id_card = info[2]
        url = "http://47.103.35.164:5002/smart/baseresidentinfo/delete"
        headers = {
            "userID": '1014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = [resident_id]
        res = requests.post(url=url, headers=headers, data=str(data))
        res_dict = res.json()
        res_code = res_dict['code']
        res_message = res_dict['message']
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)
        print("即将删除的居民id:{},居民姓名{}".format(resident_id, resident_name))

if __name__=="__main__":
    unittest.main()
