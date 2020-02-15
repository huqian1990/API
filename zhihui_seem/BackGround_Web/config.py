###项目配置文件
import os
import logging
from lib.htmlrunner import HTMLTestRunner
import time

#数据库配置
DB_API_TEST={
    'host' :'47.103.33.188',
    'user': 'root',
     'password':'123456',
     'db': 'sc_core_test',
     'charset' : 'utf8'
}

#路径配置
# os.path.abspath(__file__)   #当前文件的绝对路径
#os.path.dirname(os.path.abspath(__file__) )#当前文件的上级文件的路径
# print(os.path.abspath(__file__) )
# print(os.path.dirname(os.path.abspath(__file__) ))
BASE_DIR=os.path.dirname(os.path.abspath(__file__) )   #项目根目录
DATA_DIR=os.path.join(BASE_DIR,"data")        #数据目录
TEST_DIR=os.path.join(BASE_DIR,"test_UnitInfo")        #test目录____这里可是填写想测试的部分
LOG_DIR=os.path.join(BASE_DIR,"log")           #log目录
REPORT_DIR=os.path.join(BASE_DIR,"report")     #报告目录


#日志配置:LEVEL:级别；format:日志格式；datefmt:日期格式；handler:日志输出处理器
#asctime_当前时间  levelname：等级  filename：文件名 lineno：行数  funcName：函数名
# 日志配置  level:日志级别  format: 日志格式, datefmt 日期格式 handers 日志输出处理器
TODAY=time.strftime("%Y%m%d",time.localtime((time.time())))
cmd_hanlder=logging.StreamHandler()
LOG_FILE=os.path.join(LOG_DIR,"{}.log".format(TODAY))
file_handler=logging.FileHandler(LOG_FILE,encoding="utf-8")
logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)d] %(funcName)s: %(message)s",
                    datefmt="%Y/%m/%d %H:%M:%S",
                    handlers=[
                        # logging.StreamHandler(),  # 输出到控制台
                        # logging.FileHandler(os.path.join(BASE_DIR, 'log', "log.txt"), encoding="utf-8")  # 输出到文件

                        cmd_hanlder,file_handler
                        ]
                    )
##报告配置
REPORT_FILE=os.path.join(REPORT_DIR,'report.html')
REPORT_TILE="接口测试报告"
REPORT_DESCRIPTION="胡倩智慧社区的社区档案接口"

