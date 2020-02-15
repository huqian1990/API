from selenium import webdriver
from  time import sleep
from selenium.webdriver.common.keys import Keys
import requests


#######1.要加密的api接口中的公钥；2.请求body#######
Api_PublicKey = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCxNYUDsWfkAozT59H6xAJPmsF9Qgdjlw1MADu1lXowxvrHOOCefjPV5x47XV1g7OhrDPIPCp1rF8JL73MQh7yoUMBbcV502uoDxOqPvmAEWhZDId9Ws1G9BmzPuxYPkSMkEDVpN+fdnnMCFv/C6UE2VovUrcgNjGhpoFz6pDdH1QIDAQAB'
data='{"genreId":"mobileApp","pageNum":1,"pageSize":10}'

####获取apiSign的加密值
def get_apiSign():
    driver = webdriver.Chrome()
    driver.get("http://www.ttmd5.com/hash.php?type=9")
    driver.find_element_by_xpath("//*[@id='txtInput']").send_keys(data)
    driver.find_element_by_xpath("//*[@value=' 在 线 加 密 ']").click()
    sleep(2)
    keys = driver.find_element_by_xpath("//*[@id='divResult']").text
    apiSign = keys.split('=')[1]
    # print("生成的apiSing为{}".format(apiSign))
    return apiSign


# 获取加密data的值_____selenium没拿到数据：
'''
def get_data():
    ApiPublicKey = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCxNYUDsWfkAozT59H6xAJPmsF9Qgdjlw1MADu1lXowxvrHOOCefjPV5x47XV1g7OhrDPIPCp1rF8JL73MQh7yoUMBbcV502uoDxOqPvmAEWhZDId9Ws1G9BmzPuxYPkSMkEDVpN+fdnnMCFv/C6UE2VovUrcgNjGhpoFz6pDdH1QIDAQAB'
    driver = webdriver.Chrome()
    driver.get("http://www.bejson.com/enc/rsa/")
    driver.find_element_by_xpath("//*[@id='con1']").send_keys(ApiPublicKey)
    driver.find_element_by_xpath("//*[@id='con2']").send_keys('{"genreId":"z111111","pageNum":1,"pageSize":10}')
    sleep(3)
    driver.find_element_by_xpath("//*[@id='sels']").click()
    driver.find_element_by_xpath("//*[@class='btn-group open']/ul[@class='dropdown-menu']/li[1]").click()
    driver.find_element_by_xpath("//*[@class='btn btn-primary']").click()
    # =====已生成加密的数据，取出数据========
    data = driver.find_element_by_xpath("*[@id='result']").text
    print(data)
    driver.find_element_by_xpath("//*[@id='result']").send_keys(Keys.CONTROL, 'a')
    driver.find_element_by_xpath("//*[@id='result']").send_keys(Keys.CONTROL, 'c')
    j = driver.find_element_by_xpath("//*[@id='result']").get_attribute('value')
    print(j)
'''

####通过接口去发送请求
if __name__=="__main__":
    get_apiSign()



