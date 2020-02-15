# -*-coding:utf-8-*-
import requests
import unittest
from lib.db_conn import query_db, del_db, get_conn
import random
from lib.IdCard_gener import Carcode_gener

# 查询已登记未删除的居民信息
conn = get_conn()
residentIds = query_db(conn, "SELECT resident_id,resident_name FROM resident_info where del_flag='0'")
info = random.choice(residentIds)
resident_id = info[0]
resident_name = info[1]
lpCode = "AA{}".format(Carcode_gener())


class TestCarInfo(unittest.TestCase):
    ########添加居民车辆###########
    def test_addCar(self):
        url = "http://47.103.35.164:5002/smart/basecarinfo/save/110"
        headers = {
            "userID": '10014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = [
            {
                "residentId": resident_id,
                "lpCode": lpCode,
                "isFocus": False
            }
        ]
        res = requests.post(url=url, json=data, headers=headers)
        res_dict = res.json()
        res_code = res_dict["code"]
        res_message = res_dict["message"]
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)
        print("居民id{}姓名{}添加车牌{}成功".format(resident_id, resident_name, lpCode))

    ######查看居民车辆详情########
    def test_carinfo(self):
        url = "http://47.103.35.164:5007/api/smart/basecarinfo/info/200168"
        headers = {
            "userID": '10014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        res = requests.get(url=url, headers=headers)
        res_dict = res.json()
        res_code = res_dict["code"]
        res_message = res_dict["message"]
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)
        print("该居民添加的车辆详情为{}".format(res_dict))

    ###删除居民车辆######
    def test_delCar(self):
        conn = get_conn()
        car_id = query_db(conn, "SELECT car_id FROM car_info WHERE lp_code='{}' AND del_flag='0'".format(lpCode))
        url = "http://47.103.35.164:5002/smart/basecarinfo/delete"
        headers = {
            "userID": '10014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = [car_id[0][0]]
        res = requests.post(url=url, json=data, headers=headers)
        res_dict = res.json()
        res_code = res_dict["code"]
        res_message = res_dict["message"]
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)
        print("删除居民{}的车牌{}成功".format(resident_name, car_id[0][0]))

    #####查看社区车辆列表######
    def test_carList(self):
        url = "http://47.103.35.164:5002/smart/basecarinfo/pagelist"
        headers = {
            "userID": '10014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = {
            "pcStatus": "True",
            "pcType": "",
            "pageNum": 1,
            "pageSize": 10
        }
        res = requests.post(url=url, json=data, headers=headers)
        res_dict = res.json()
        res_code = res_dict["code"]
        res_message = res_dict["message"]
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)
        print("社区车辆列表为{}".format(res_dict))

if __name__ == "__main__":
    unittest.main()
