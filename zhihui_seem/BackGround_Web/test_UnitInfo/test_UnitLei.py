import requests
import unittest
from lib.db_conn import query_db,del_db,get_conn



#添加设备类型的名称和标识
deviceTypeName="TEST"
remark="API接口TEST"

class Test_Unit_Leibie(unittest.TestCase):
    def test_Unit_Leibie_Add(self):
        url = "http://47.103.35.164:5002/smart/communitydevicetypeinfo/v1/batchSaveOrUpdate"
        headers = {
            "userID": '10014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = {
            "deviceTypeObjs": [
                {
                    "deviceTypeName": deviceTypeName,
                    "remark": remark
                }
            ]
        }
        res = requests.post(url=url, json=data, headers=headers)
        res_dict = res.json()
        res_code=res_dict["code"]
        res_message=res_dict["message"]
        self.assertEqual("200",res_code)
        self.assertEqual("成功",res_message)
        print("添加监控点名称为{}编号为{}".format(deviceTypeName, type))

    def test_Unit_Leibie_List(self):
        url = "http://47.103.35.164:5002/smart/communitydevicetypeinfo/v1/list"
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

    def test_Unit_Leibie_Del(self):
        #找出添加的设备的
        conn=get_conn()
        result=query_db(conn,"SELECT id FROM device_type_info WHERE device_type_name='{}' AND del_flag='0'".format(deviceTypeName))
        url = "http://47.103.35.164:5002/smart/communitydevicetypeinfo/v1/delete"
        headers = {
            "userID": '10014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = {
            "id": result[0][0]
        }
        res = requests.post(url=url, json=data, headers=headers)
        res_dict = res.json()
        res_code = res_dict["code"]
        res_message = res_dict["message"]
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)

if __name__=="__main__":
    unittest.main()