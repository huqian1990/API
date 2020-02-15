import requests
#######直接CPOY的postman######______有时候好有时坏的
# url='http://api.bejson.com/btools/tools/enc/rsa/buildRSAEncryptByPublicKey'
# payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"key\"\r\n\r\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCxNYUDsWfkAozT59H6xAJPmsF9Qgdjlw1MADu1lXowxvrHOOCefjPV5x47XV1g7OhrDPIPCp1rF8JL73MQh7yoUMBbcV502uoDxOqPvmAEWhZDId9Ws1G9BmzPuxYPkSMkEDVpN+fdnnMCFv/C6UE2VovUrcgNjGhpoFz6pDdH1QIDAQAB\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"data\"\r\n\r\n{\"genreId\":\"mobileApp\",\"pageNum\":1,\"pageSize\":10}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"rsaType\"\r\n\r\nrsa\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
# headers = {
#     'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
#     'Content-Type': "application/json",
#     'cache-control': "no-cache",
#     'Postman-Token': "1554b566-ff07-4b82-b231-437f028c1d36"
#     }
# res=requests.post(url=url, data=payload, headers=headers)
# print(res.text)


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
    print("生成的apiData为{}".format(res_dict['message']))
    return res_dict['message']






