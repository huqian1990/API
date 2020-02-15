import requests
import unittest



class Test_OpenApi(unittest.TestCase):
    #####获取配置项列表
    def test_configeList(self):
        url = "http://47.103.37.193:8280/open/v1/config/list"
        headers = {"userId": "huqian",
                   "apiConfigId": "PZ00000010",
                   "apiSign": "b2cee5c1e4dd452c862c7b2499cba7f478248a9f8bf54c339c5dcba9db9e33ac",
                   "ip": "192.168.11.11",
                   "purpose": "",
                   "Content-Type": "application/json"
                   }
        data = 'mdT3coHQxzpKrsPt86YaFgQf0G+K1IdLgGbiKQRvjXCsZt0WxEfVyXi4lGuiNszWmOvBKqg95z41UvFt5S8d0ggdmzRl5W8LT5317pjkPD9EdkqBPt2nGP65BZRTKTBA1GpYEjFlFWv3xsaN4MBJztR4xv/PBmIFtnotRhhKDH0='
        res = requests.post(url=url, headers=headers, json=str(data))
        print(res.json())
    # 获取配置项属性列表
    def test_configList_shuxing(self):
        url = "http://47.103.37.193:8280/open/v1/config/propertylist"
        headers = {"userId": "huqian",
                   "apiConfigId": "PZ00000010",
                   "apiSign": "16d5ed2d1fbe79e0756ae5f3d19124cf5937bd2dafd9bd8072923d8bbf0aca83",
                   "ip": "192.168.11.11",
                   "purpose": "",
                   "Content-Type": "application/json"
                   }
        data = 'MvBHW3EYl3LLMrduONmgzapWlsopps8shps1it8d9b4olVn+fKOjqCuHCY+f/ZGTvxfuuhM/ZjYEBvJnCXgZuqRmo0fzD/1y229d0EKsb6SQ2+b16js5RoJj2l7D3Q3Xm/zcXH0+RaFQqEOjipDyjyrp4vWGeiiWOnrDR++YsNI='
        res = requests.post(url=url, headers=headers, json=data)
        print(res.json())

    ###配置项关系查询
    def test_congfigRelation(self):
        url = "http://47.103.37.193:8280/open/v1/config/relations"
        headers = {"userId": "huqian",
                   "apiConfigId": "PZ00000010",
                   "apiSign": "16d5ed2d1fbe79e0756ae5f3d19124cf5937bd2dafd9bd8072923d8bbf0aca83",
                   "ip": "192.168.11.11",
                   "purpose": "",
                   "Content-Type": "application/json"
                   }
        data = 'MvBHW3EYl3LLMrduONmgzapWlsopps8shps1it8d9b4olVn+fKOjqCuHCY+f/ZGTvxfuuhM/ZjYEBvJnCXgZuqRmo0fzD/1y229d0EKsb6SQ2+b16js5RoJj2l7D3Q3Xm/zcXH0+RaFQqEOjipDyjyrp4vWGeiiWOnrDR++YsNI='
        res = requests.post(url=url, headers=headers, json=data)
        print(res.json())

    ###修改单个配置项属性
    def test_singleConfig_shuxing(self):
        url = "http://47.103.37.193:8280/open/v1/config/update"
        headers = {"userId": "huqian",
                   "apiConfigId": "PZ00000010",
                   "apiSign": "1bd09ea4235040a3fd682e14d97c11924c33e058da1a34dd5af6cf0a69721f5f",
                   "ip": "192.168.11.11",
                   "purpose": "",
                   "Content-Type": "application/json"
                   }
        data = 'TUesIeXDIeXD84Pl40VvvDM/L5oCY8dAfQK8DGAU7jyTzBxY9tx5ZPeQRdiFlC3Z3OttfPV5NJQtGa2E7FOMhZDeqr7T6c6bhNqUaffW4IENUaykPMNrtDJyHW4Gu0E5SuI/kQlqBBYqmxoSRLlic7QLCUf6zJ6Y6VHQRhWFIhM='
        res = requests.post(url=url, headers=headers, json=data)
        print(res.json())

    ####获得配置项模型
    def test_configeModule(self):
        url = "http://47.103.37.193:8280/open/v1/config/update"
        headers = {"userId": "huqian",
                   "apiConfigId": "PZ00000010",
                   "apiSign": "cfb964db783434021792f5ddeb61a9e940849155ce6e21fa8325adcf07cfa031",
                   "ip": "192.168.11.11",
                   "purpose": "",
                   "Content-Type": "application/json"
                   }
        data = 'kQptvsgqRFtqksrZQsnMyt7Mkh3ApZ/vrcJmubekz7yJlOhaF6BBFCVAPCpbGpYRdaEtm6Nq/eKXdQ9q2vsdWcS945ciLnL5/FY9gdcxYn0fwDDLz2oLW1EL22BkSol/+d0zTYsv1BRahGo3BXV45d+VlxBSqAixTYSVj6ruOro='
        res = requests.post(url=url, headers=headers, json=data)
        print(res.json())

    ####获得配置项单个属性
    def test_configeSingle_shuxing(self):
        url = "http://47.103.37.193:8280/open/v1/config/getModel"
        headers = {"userId": "huqian",
                   "apiConfigId": "PZ00000010",
                   "apiSign": "29ed7b319fa04946ee4eeff1350eac714c0d2294503c329b0f4c4af6a74fb332",
                   "ip": "192.168.11.11",
                   "purpose": "",
                   "Content-Type": "application/json"
                   }
        data = 'sGtcVKLmCN1oQoKH/Uhex7BT45E8JsjiaR9y3DXEn3alNH5ig8DKNl2LbS6eihxMstI5OA1kFXmaCBJqCzcssCKnbzPqQtCOfnANm6G6ejn8lPLo0mz86BqqvowYwE4Wo3s+CXKO3XFQbU0WeUbMsspZoBw1/+IVvd0/5J0k8D8='
        res = requests.post(url=url, headers=headers, json=data)
        print(res.json())


if __name__=="__main__":
    unittest.main()