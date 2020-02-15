import requests
import unittest
from lib.db_conn import query_db, del_db, get_conn


#==========社区服务API==========
class Test_Sevice(unittest.TestCase):
    def test_addsevice(self):
        url = "http://47.103.35.164:5002/web/serviceBuildInfo/v1/saveOrUpdate"
        headers = {
            "userID": '10014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = {
            "address": "上海市宝山区央行正12301",
            "carPark": "A1-A12",
            "contactTel": "15952330194",
            "name": "王雄鲜花室",
            "pic": "王熊",
            "coordinate": "S12，N121",
            "remark": "处理各类居民事物，欢迎光临",
            "serviceTime": "周一至周五：8:00-11:00,14:00-18:00；",
            "type": "1"
        }
        res = requests.post(url=url, json=data, headers=headers)
        res_dict = res.json()
        res_code = res_dict["code"]
        res_message = res_dict["message"]
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)
        print("添加社区服务成功")

    def test_delsevice(self):
        ###删除社区服务——可以修改社区服务的名字；
        conn = get_conn()
        result = query_db(conn, "SELECT id FROM service_build_info where name='王雄鲜花室' and del_flag='0'")
        url = "http://47.103.35.164:5002/web/serviceBuildInfo/v1/delete"
        headers = {
            "userID": '10014',
            "loginName": 'huqian',
            "communityId": "201901",
            "Content-Type": "application/json"
        }
        data = [result[0][0]]
        res = requests.post(url=url, data=str(data), headers=headers)
        res_dict = res.json()
        res_code = res_dict["code"]
        res_message = res_dict["message"]
        self.assertEqual("200", res_code)
        self.assertEqual("成功", res_message)
        print("删除社区服务{}成功".format("王雄鲜花室"))

    def test_serviceList(self):
        url = "http://47.103.35.164:5002/web/serviceBuildInfo/v1/pageList"
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
        print("社区服务列表如下{}".format(res_dict))



if __name__ == "__main__":
    unittest.main()
