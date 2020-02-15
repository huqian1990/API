import requests
import unittest
from config import DB_API_TEST
from lib.db_conn import query_db, del_db
from lib.db_conn import query_db, del_db, get_conn
import pymysql
from config import DB_API_TEST

# 添加设备
deviceName = "TEST_deviceName"
deviceCode = "TEST_deviceId"
deviceAdress = "123.01S,145,21N"


class Test_Unit_Shebei(unittest.TestCase):
    def test_Unit_Shebei_Add(self):
        url = "http://47.103.35.164:5002/smart/communitydeviceinfo/v1/saveOrUpdate"
        headers = {
            "userID": '10014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = {
            "address": deviceAdress,
            "deviceCode": deviceCode,
            "deviceName": deviceName
        }
        res = requests.post(url=url, json=data, headers=headers)
        res_dict = res.json()
        res_code = res_dict["code"]
        res_message = res_dict["message"]
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)
        print("添加的设备名称为{}，编号为{}，地址为{}".format(deviceName, deviceCode, deviceAdress))

    def test_Unit_Shebei_List(self):
        url = "http://47.103.35.164:5002/smart/communitydeviceinfo/v1/pageList"
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
        print("设备列表为{}".format(res_dict))

    def test_Unit_Shebei_Nums(self):
        url = "http://47.103.35.164:5002/smart/communitydeviceinfo/v1/deviceCount"
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
        print("共有设备数量为{}".format(res_dict["data"]))

    def test_Unit_Shebei_Del(self):
        # 查找添加的设备
        conn = get_conn()
        ids = query_db(conn, "SELECT id FROM device_info WHERE device_name='{}' AND del_flag='0'".format(deviceName))
        url = "http://47.103.35.164:5002/smart/communitydeviceinfo/v1/batchDel"
        headers = {
            "userID": '1014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = {
            "ids": [
                ids[0][0]
            ]
        }
        res = requests.post(url=url, json=data,headers=headers)
        res_dict = res.json()
        res_code = res_dict["code"]
        res_message = res_dict["message"]
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)
        print("删除的设备为'{}'".format(deviceName))


#####设备的数据导出#####
   # def test_Unit_Shebei_Export(self):
        url = "http://47.103.35.164:5002/smart/communitydeviceinfo/v1/export"
        headers = {
            "userID": '10014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = {  }
        res = requests.post(url=url, json=data,headers=headers)
        res_dict = res.json()
        res_code = res_dict["code"]
        res_message = res_dict["message"]
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)



if __name__ == "__main__":
    unittest.main()
