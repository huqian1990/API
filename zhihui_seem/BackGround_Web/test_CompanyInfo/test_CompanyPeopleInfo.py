import json
import pymysql
import requests
from lib.db_conn import query_db, get_conn, del_db
import unittest

# 环境准备
conn = get_conn()
result = query_db(conn, "SELECT company_id FROM company_info WHERE company_name='Test阿里巴巴商务公司' and del_flag='0'")
class Test_CompanyPeople(unittest.TestCase):
    def test_addCompanyPeople(self):
        url = "http://47.103.35.164:5002/smart/baseComMemberinfo/save"
        headers = {
            "userID": '10014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = {
            "companyId": str(result[0][0]),
            "contactPhone": "15849338388",
            "idCard": "321292000399939299",
            "memberName": "小蜜桃",
            "sex": "女",
            "pictureUrl": "1.jpg "
        }
        res = requests.post(url=url, headers=headers, json=data)
        res_dict = res.json()
        res_code = res_dict['code']
        res_message = res_dict['message']
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)

    #####单位成员列表######
    def test_companyPeople_list(self):
        url = "http://47.103.35.164:5002/smart/baseComMemberinfo/pagelist"
        headers = {
            "userID": '10014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = {
            "companyId": str(result[0][0]),
            "pageNum": 1,
            "pageSize": 10
        }
        res = requests.post(url=url, headers=headers, json=data)
        res_dict = res.json()
        res_code = res_dict['code']
        res_message = res_dict['message']
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)
        print("该单位的成员列表为{}".format(res_dict))

    #####单位成员的删除
    def test_delCompanyPeople(self):
        # 数据库查询新添加的公司
        conn = get_conn()
        result1 = query_db(conn, "SELECT member_id FROM company_member_info WHERE  company_id='{}'and del_flag='0'".format(result[0][0]))
        print(result1)
        url="http://47.103.35.164:5002/smart/baseComMemberinfo/delete"
        headers = {
            "userID": '10014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data=[result1[0][0]]
        res = requests.post(url=url, headers=headers, data=str(data))
        res_dict = res.json()
        res_code = res_dict['code']
        res_message = res_dict['message']
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)


if __name__ == "__main__":
    unittest.main()


