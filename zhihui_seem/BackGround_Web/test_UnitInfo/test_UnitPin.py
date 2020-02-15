import requests
import unittest
from  lib.db_conn import query_db,del_db
from config import DB_API_TEST
from lib.db_conn import query_db, del_db,get_conn
import pymysql
from config import DB_API_TEST

#添加
deviceBrandCode="TEST_deviceBandCode"
deviceBrandName="TEST_deviceBand"

class TestUnitPinpai(unittest.TestCase):
    def test_Unit_Pinpai_Add(self):
        url = "http://47.103.35.164:5002/smart/communitydevicebrandinfo/v1/saveOrUpdate"
        headers = {
            "userID": '10014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = {
            "deviceBrandCode": deviceBrandCode,
            "deviceBrandName": deviceBrandName
        }
        res = requests.post(url=url, json=data, headers=headers)
        res_dict = res.json()
        res_code = res_dict["code"]
        res_message = res_dict["message"]
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)
        print("添加设备品牌名称为{}编号为{}".format(deviceBrandName, deviceBrandCode))

    def test_Unit_Pinpa_List(self):
        url = "http://47.103.35.164:5002/smart/communitydevicebrandinfo/v1/pageList"
        headers = {
            "userID": '10014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = {
            "pageNum": 1,
            "pageSize": 10
        }
        res = requests.post(url=url, json=data, headers=headers)
        res_dict = res.json()
        res_code = res_dict["code"]
        res_message = res_dict["message"]
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)
        print("设备品牌列表如下{}".format(res_dict))

    def test_Unit_Pinpa_Del(self):
        #找出刚添加的设备品牌的ID
        conn=get_conn()
        ids=query_db(conn,"SELECT id FROM device_brand_info WHERE device_brand_name='{}' AND del_flag='0'".format(deviceBrandName))
        brandIds=query_db(conn,"SELECT device_brand_id FROM device_brand_info WHERE device_brand_name='{}' AND del_flag='0'".format(deviceBrandName))
        print(ids,brandIds)
        url = "http://47.103.35.164:5002/smart/communitydevicebrandinfo/v1/batchDel"
        headers = {
            "userID": '10014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = {
            "brandIds": [
                brandIds[0][0]
            ],
            "ids": [
               ids[0][0]
            ]
        }
        res = requests.post(url=url, json=data, headers=headers)
        res_dict = res.json()
        res_code = res_dict["code"]
        res_message = res_dict["message"]
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)
        print("删除设备品牌'{}'成功".format(deviceBrandName))

if __name__=="__main__":
    unittest.main()