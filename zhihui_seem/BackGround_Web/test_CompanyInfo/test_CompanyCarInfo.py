import requests
import unittest
from lib.db_conn import get_conn, query_db, del_db

# 环境准备——可修改这边的company_name
conn = get_conn()
companyId = query_db(conn, "SELECT company_id FROM company_info WHERE company_name='Test阿里巴巴商务公司' and del_flag='0'")
class Test_Company(unittest.TestCase):
    def test_addcompany(self):
        ###########添加单位车辆信息############################
        # 组装和发送请求
        if companyId:
            url = "http://47.103.35.164:5002/smart/basecompanyinfo/saveOrUpdateCar"
            headers = {
                "userID": '10014',
                "loginName": 'huqian',
                "communityId": "201901",
                "Content-Type": "application/json"
            }
            data = [
                {
                    "carBrand": "AAA",
                    "carColour": "Black",
                    "companyId": companyId[0][0],
                    "focus": True,
                    "isFocus": False,
                    "lpCode": "SA123456",
                    "lpExpireDate": "2019-10-31"
                }
            ]
            res = requests.post(url=url, headers=headers, json=data)
            res_dict = res.json()
            res_code = res_dict['code']
            res_message = res_dict['message']
            self.assertEqual("200", res_code)
            self.assertEqual("成功", res_message)
        else:
            print("公司不存在或者已经删除")


    ######车辆信息列表
    def test_companycarList(self):
     if companyId:
         url = "http://47.103.35.164:5002/smart/basecompanyinfo/car/pagelist"
         headers = {
             "userID": '10014',
             "loginName": 'huqian',
             "communityId": "201901",
             "Content-Type": "application/json"
         }
         data = {
             "companyId": companyId[0][0],
             "pageNum": 1,
             "pageSize": 10
         }
         res = requests.post(url=url, headers=headers, json=data)
         res_dict = res.json()
         res_code = res_dict['code']
         res_message = res_dict['message']
         self.assertEqual("200", res_code)
         self.assertEqual("成功", res_message)
         print(res_dict)
     else:
         print("公司不存在或者已经删除")

####删除单位车辆
    def test_delcompanycar(self):
        ###查找公司车辆
        conn=get_conn()
        companyCarId=query_db(conn,"SELECT car_id FROM car_info WHERE company_id='{}' and del_flag='0'".format(companyId[0][0]))
        if companyCarId:
            url = "http://47.103.35.164:5002/smart/basecarinfo/delete"
            headers = {
                "userID": '10014',
                "loginName": 'huqian',
                "communityId": "201901",
                "Content-Type": "application/json"
            }
            data = [companyCarId[0][0]]
            res = requests.post(url=url, headers=headers, data=str(data))
            res_dict = res.json()
            res_code = res_dict['code']
            res_message = res_dict['message']
            self.assertEqual("200", res_code)
            self.assertEqual("成功", res_message)
        else:
            print("公司不存在或者没有该车信息")
if __name__=="__main__":
    unittest.main()


