#-*-coding:utf-8-*-
#数据库封装方法#
import requests
import json
from jsonpath import jsonpath
import pymysql
from config import DB_API_TEST
import unittest
from lib.db_conn import get_conn,query_db,del_db
from lib.IdCard_gener import IdCard_gener,PhoneNum_gener
import random

Update_IdCard=IdCard_gener()
Update_PhoneNum=PhoneNum_gener()
print("修改居民的身份证号为：{}".format(Update_IdCard))
print("修改居民的手机号为：{}".format(Update_PhoneNum))
conn = get_conn()
result = query_db(conn, "SELECT resident_id FROM resident_info")
resident_id=random.sample(result,1)
new_resident_id=resident_id[0][0]


class Tesrt_Update(unittest.TestCase):

    def test_UpdateInfo(self):
        url = "http://47.103.35.164:5002/smart/baseresidentinfo/detailForUpdate"
        headers = {
            "userID": '1014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = {
            "communityId": 201901,
            "houseId": 0,
            "residentId": new_resident_id
        }
        res = requests.post(url=url, headers=headers, json=data)
        res_dict=res.json()
        res_residentId = res_dict['data']['baseInfo']['residentId']
        res_residentName = res_dict['data']['baseInfo']['residentName']
        res_idCard = res_dict['data']['baseInfo']['idCard']
        print("旧的居民号是{}，姓名是{}，身份证号{}".format(res_residentId, res_residentName, res_idCard))


    def test_UpdateInfo_Add(self):
        print("=====开始修改居民信息======")
        # 修改居民信息
        url = "http://47.103.35.164:5002/smart/baseresidentinfo/save"
        headers = {
            "userID": '1014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = {
            "birthday": "1999-10-31",
            "censusRegister": {
                "city": "市辖区",
                "cityId": "120100",
                "county": "河西区",
                "countyId": "120103",
                "province": "天津市",
                "provinceId": "120000"
            },
            "censusRegisterDetailAddress": "江苏省扬州市淮阴县吹纷争1204室",
            "communityId": 201901,
            "contactPhone": Update_PhoneNum,
            "createBy": "string",
            "education": "大学",
            "id": 0,
            "idCard": Update_IdCard,  # 判断居民唯一标识
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
            "residentId": new_resident_id,
            "residentName": "王小明",
            "sex": "1",
            "workUnit": "上海腾讯科技有限公司商务部"
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.json())
        res_dict = res.json()
        res_code = res_dict['code']
        res_message = res_dict['message']
        res_residentId = res_dict['data']['residentId']
        res_residentName = res_dict['data']['residentName']
        res_idCard = res_dict['data']['idCard']
        print("修改后的居民residentId:{}".format(res_residentId))
        print("修改后的residentName:{}".format(res_residentName))
        print("修改后的res_idCard:{}".format(res_idCard))

if __name__=="__main__":
    unittest.main()


















