import requests
import unittest
import jsonpath
from config import DB_API_TEST
from lib.db_conn import query_db, del_db,get_conn
import pymysql
from config import DB_API_TEST
# 添加监控点的名称和编号
monitorPointCode = "AreaDoor"
monitorPointName = "小区大门"

class Test_Unit_Jiankong(unittest.TestCase):
    def test_add_Unit_Jiankong(self):
        url = "http://47.103.35.164:5002/smart/communitymonitorpointinfo/v1/saveOrUpdate"
        headers = {
            "userID": '10014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = {
            "monitorPointCode": monitorPointCode,
            "monitorPointName": monitorPointName
        }
        res = requests.post(url=url, json=data, headers=headers)
        res_dict=res.json()
        res_code = res_dict["code"]
        res_message = res_dict["message"]
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)
        print("添加监控点名称为{}编号为{}".format(monitorPointCode,monitorPointName))


    def test_list_Unit_Jiankong(self):
        url = "http://47.103.35.164:5002/smart/communitymonitorpointinfo/v1/pageList"
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
        print("监控点列表如下{}".format(res_dict))

    def test_Unit_Jiankong_Del(self):
        #######删除刚刚添加的监控点
        conn = get_conn()
        result = query_db(conn, "SELECT id FROM monitor_point_info WHERE  monitor_point_name='{}'AND del_flag='0'".format(monitorPointName))
        print(result)
        url = "http://47.103.35.164:5002/smart/communitymonitorpointinfo/v1/batchDel"
        headers = {
            "userID": '10014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = {
            "ids": [
               result[0][0]
            ]
        }
        res = requests.post(url=url, json=data, headers=headers)
        res_dict = res.json()
        res_code = res_dict["code"]
        res_message = res_dict["message"]
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)
        print("设备监控点{}已删除".format(monitorPointName))

if __name__=="__main__":
    unittest.main()