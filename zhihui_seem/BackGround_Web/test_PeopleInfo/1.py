import requests
import jsonpath
import random
from config import DB_API_TEST
from lib.db_conn import query_db, del_db, get_conn
import pymysql
from config import DB_API_TEST
#
# deviceName = "TEST_deviceName"
# conn = get_conn()
# conn = get_conn()
#
# # url = "http://47.103.35.164:5002/smart/communitymonitorpointinfo/v1/batchDel"
# # headers = {
# #     "userID": '10014',
# #     "loginName": 'huqian',
# #     "communityId": "201901",
# #     "Content-Type": "application/json"
# # }
# # data = {
# #     "ids": [
# #        result
# #     ]
# # }
# # res = requests.post(url=url, json=data, headers=headers)
# # res_dict = res.json()
# # res_code = res_dict["code"]
# # res_message = res_dict["message"]
# # self.assertEqual("200", res_code)
# # self.assertEqual("成功", res_message)
#
# deviceGroupName = "Test_deviceGroupName"
# remark = "Test_deviceGroupRemark"
# url = "http://47.103.35.164:5002/smart/communitydevicegroupinfo/v1/saveOrUpdate"
# headers = {
#     "userID": '10014',
#     "loginName": 'huqian',
#     "communityId": "201901",
#     "Content-Type": "application/json"
# }
# data = {
#     "deviceGroupObjs":
#         [
#             {
#                 "deviceGroupName": deviceGroupName,
#                 "remark": remark
#
#             }
#         ]
# }
# res = requests.post(url=url, json=data, headers=headers)
# res_dict = res.json()
# print(res_dict)
conn = get_conn()
result=query_db(conn,"SELECT resident_id,resident_name,id_card FROM resident_info WHERE del_flag='0'")
info=random.choice(result)
print(info)
print(info[0])
print(info[1])
print(info[2])