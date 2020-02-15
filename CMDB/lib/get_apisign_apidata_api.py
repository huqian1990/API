import requests


######直接通过接口去获取到加密数据
def get_apiData():
    url = 'http://api.bejson.com/btools/tools/enc/rsa/buildRSAEncryptByPublicKey'
    key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCxNYUDsWfkAozT59H6xAJPmsF9Qgdjlw1MADu1lXowxvrHOOCefjPV5x47XV1g7OhrDPIPCp1rF8JL73MQh7yoUMBbcV502uoDxOqPvmAEWhZDId9Ws1G9BmzPuxYPkSMkEDVpN%2BfdnnMCFv%2FC6UE2VovUrcgNjGhpoFz6pDdH1QIDAQAB'
    data = '{"genreId":"mobileApp","pageNum":1,"pageSize":10}'
    rsaType = 'rsa'
    payload = ('key=') + key + '&' + ('data=') + data + '&' + ('rsaType=') + rsaType
    # payload = "key=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCxNYUDsWfkAozT59H6xAJPmsF9Qgdjlw1MADu1lXowxvrHOOCefjPV5x47XV1g7OhrDPIPCp1rF8JL73MQh7yoUMBbcV502uoDxOqPvmAEWhZDId9Ws1G9BmzPuxYPkSMkEDVpN%2BfdnnMCFv%2FC6UE2VovUrcgNjGhpoFz6pDdH1QIDAQAB&data=%7B%22genreId%22%3A%22mobileApp%22%2C%22pageNum%22%3A1%2C%22pageSize%22%3A10%7D&rsaType=rsa&undefined="
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache"
    }
    res = requests.post(data=payload, headers=headers, url=url)
    res_dict = res.json()
    # print("生成的apiData为{}".format(res_dict['message']))
    return res_dict['message']


if __name__=="__main__":
    get_apiData()