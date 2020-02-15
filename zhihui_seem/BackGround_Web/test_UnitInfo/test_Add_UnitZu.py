import requests
import unittest
from lib.db_conn import query_db, del_db, get_conn
import pymysql
from config import DB_API_TEST
import time

##添加设备分组
deviceGroupName = "Test_deviceGroupName"
remark = "Test_deviceGroupRemark"

class Test_Unit_Fenzu(unittest.TestCase):
    def test_Unit_Fenzu_Add(self):
        url = "http://47.103.35.164:5002/smart/communitydevicegroupinfo/v1/saveOrUpdate"
        headers = {
            "userID": '10014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = {
            "deviceGroupObjs":
                [
                    {
                        "deviceGroupName": deviceGroupName,
                        "remark": remark

                    }
                ]
        }
        res = requests.post(url=url, json=data, headers=headers)
        res_dict = res.json()
        res_code = res_dict["code"]
        res_message = res_dict["message"]
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)
        print("添加设备品牌名称为{}标识为{}".format(deviceGroupName, remark))




    def test_Unit_Fenzu_List(self):
        url = "http://47.103.35.164:5002/smart/communitydevicegroupinfo/v1/list"
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
        res = requests.post(url=url, headers=headers, json=data)
        res_dict = res.json()
        res_code = res_dict["code"]
        res_message = res_dict["message"]
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)
        print("设备分组列表名为{}".format(res_dict))

    time.sleep(5)


    def test_DelUnit_Feizu_(self):
        # 查找添加的设备分组
        conn = get_conn()
        result=query_db(conn,"SELECT * FROM device_group_info WHERE device_group_name='{}'and del_flag='0'".format(deviceGroupName))
        print(result)

        ids = query_db(conn,"SELECT id FROM device_group_info WHERE device_group_name='{}'and del_flag='0'".format(deviceGroupName))
        print(ids)
        url = "http://47.103.35.164:5002/smart/communitydevicegroupinfo/v1/batchDel"
        headers = {
            "userID": '10014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = {
            "id": "{}".format(ids[0][0])
        }
        res = requests.post(url=url, headers=headers, json=data)
        res_dict = res.json()
        res_code = res_dict["code"]
        res_message = res_dict["message"]
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)
        print("删除的设备分组为{}".format(deviceGroupName))


if __name__ == "__main__":
    unittest.main()
