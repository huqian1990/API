#-*-coding:utf-8-*-
#数据库封装方法#
import requests
import unittest
from lib.db_conn import get_conn,query_db,del_db
from lib.IdCard_gener import IdCard_gener

#新建新的居民身份证号
NEW_IdCard=IdCard_gener()
print("新居民的身份证号为：{}".format(NEW_IdCard))

# 编写一个测试类，以test开头，继承unittest.TestCase
class TestAdd(unittest.TestCase):
    # 编写具体的测试用例方法
    def test_add_PeopleInfo(self):
        session = requests.session()
        # 环境监察以及数据准备:居民身份证是否已录入
        conn = get_conn()
        result= query_db(conn,"SELECT * FROM resident_info WHERE id_card='{}'".format((NEW_IdCard)))
        if result:
            del_db(conn,"DELETE FROM resident_info WHERE id_card ='{}'".format((NEW_IdCard)))
###########添加居民信息############################
        print("=================添加居民信息===========")
        url = "http://47.103.35.164:5002/smart/baseresidentinfo/save"
        headers = {
            "userID": '1014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = {
            "birthday": "1991-10-31",
            "censusRegister": {
                "city": "市辖区",
                "cityId": "120100",
                "county": "河西区",
                "countyId": "120103",
                "province": "天津市",
                "provinceId": "120000"
            },
            "censusRegisterDetailAddress": "上海市嘉定区龙翔正赵华小区12栋1203室",
            "communityId": 201901,
            "contactPhone": "18888888888",
            "createBy": "string",
            "education": "大学",
            "id": 0,
            "idCard":NEW_IdCard,  # 判断居民唯一标识
            "isFocus": 'false',
            "isMarry": "已婚",
            "nation": "汉族",
            "nationality": "中国大陆",
            "poc": "群众",
            "profession": "文化传媒",
            "remark": "string",
            "resideInfoList": [
                {
                    "houseId": 0,
                    "houseLevelDTOS": [
                        {
                            "level": "H",
                            "levelId": 42,
                            "name": "string"
                        }
                    ],
                    "relationType": "1",
                    "resideInfoId": 0,
                    "residePeriod": "string",
                    "resideReason": "8",
                    "resideStatus": "0",
                    "userId": 0
                }
            ],
            "residentId": 0,
            "residentName": "胡小丹",
            "sex": "1",
            "workUnit": "上海鼓楼科技有限公司"
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.json())
        res_dict = res.json()
        res_code = res_dict['code']
        res_message = res_dict['message']
        res_residentId = res_dict['data']['residentId']
        res_residentName = res_dict['data']['residentName']
        res_idCard = res_dict['data']['idCard']
        self.assertEqual("200", res_code)
        self.assertEqual(u"成功", res_message)
        print("居民号是{}，姓名是{}，身份证号{}".format(res_residentId,res_residentName,res_idCard) )


    def test_query_PeopleList(self):
        print("=============查看添加的居民详情信息=============")
        conn = get_conn()
        resident_id = query_db(conn, "SELECT resident_id FROM resident_info WHERE  id_card='{}'".format(NEW_IdCard))
        print("查询的居民ID为{}的详情信息".format(resident_id[0][0]))
        url = "http://47.103.35.164:5002/smart/baseresidentinfo/detail"
        headers = {
            "userID": '1014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = {
            "communityId": 201901,
            "houseId": 0,
            "residentId": resident_id[0][0]
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.json())
        # 数据清理——数据库清理【删除添加的居民信息】
        del_db(conn, "DELETE FROM resident_info WHERE  id_card='{}'".format(NEW_IdCard))
        result1 = (conn, "SELECT resident_id FROM resident_info WHERE  id_card='{}'".format(NEW_IdCard))
        print(result1)
        print("删除成功，数据不存在")
if __name__=="__main__":
    unittest.main()





































