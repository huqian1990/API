import json
import pymysql
import requests
from lib.db_conn import query_db, get_conn, del_db
import unittest



####社区的单位名称等等都不做校验——可以写死

# 设置公司名称
class Test_Company(unittest.TestCase):
    def test_addcompany(self):
        ###########添加单位信息############################
        # 组装和发送请求
        url = "http://47.103.35.164:5002/smart/baseresidentinfo/save"
        headers = {
            "userID": '10014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = {
            "companyName": "Test社区单位阿里巴巴",
            "busLic": "HsWOAINI1997",
            "busLicPictureUrl": "2.jpeg",
            "legalIdentityCard": "321029199811071123",
            "legalPerson": "马爸爸",
            "legalPhone": "13922222222",
            "legalPicture": "h1.jpeg",
            "legelAddress": "杭州市上城区阿里巴巴大楼1206室",
            "operatorPeriod": ["2019-11-07T06:36:54.801Z", "2019-12-19T06:36:54.801Z"],
            "address": "江桥镇天际蓝桥08栋1204室"
        }
        res = requests.post(url=url, headers=headers, data=json.dumps(data))
        res_dict = res.json()
        res_code = res_dict['code']
        res_message = res_dict['message']
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)
        # 数据库查询新添加的公司
        conn = get_conn()
        result = query_db(conn, "SELECT * FROM company_info WHERE company_name='{}'".format('Test阿里巴巴商务公司'))
        if result:
            print("添加新公司成功，公司名称为{}".format())
        else:
            print("添加公司失败")

###########单位列表#########
    def test_companyList(self):
        url = "http://47.103.35.164:5002/smart/basecompanyinfo/pagelist"
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
        res_code = res_dict['code']
        res_message = res_dict['message']
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)
        print("社区单位列表为{}".format(res_dict))


    ########删除单位信息#############
    def test_delCompany(self):
        # 数据库查询新添加的公司
        conn = get_conn()
        result = query_db(conn, "SELECT company_id FROM company_info WHERE company_name='{}' and del_flag='0'".format(
            'Test阿里巴巴商务公司'))
        url = "http://47.103.35.164:5002/smart/basecompanyinfo/delete"
        headers = {
            "userID": '10014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = [result[0][0]]
        print(data)
        res = requests.post(url=url, headers=headers, data=str(data))
        print(res.json())
        res_dict = res.json()
        res_code = res_dict['code']
        res_message = res_dict['message']
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)
        print("删除单位{}成功".format("Test阿里巴巴商务公司"))
if __name__ == "__main__":
    unittest.main()
