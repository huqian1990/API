from selenium import webdriver
from  time import sleep
from selenium.webdriver.support.ui import WebDriverWait
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
driver = webdriver.Chrome(options=option) # # 打开chrome浏览器
# 改动打开浏览器
driver.get("http://47.103.35.164:5007/user/login")
driver.maximize_window()


#登录
def log_in(username, password):
    driver.find_element_by_id("loginName").send_keys(username)
    driver.find_element_by_id('passWord').send_keys(password)
    driver.find_element_by_xpath('//form//button').click()
    sleep(3)


if __name__ == "__main__":
        log_in("huqian", "123456")












