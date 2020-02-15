import unittest
import logging
from config import TEST_DIR,BASE_DIR,REPORT_DIR,REPORT_FILE,REPORT_DESCRIPTION
from lib.htmlrunner import HTMLTestRunner
import os
def main():
    suite=unittest.defaultTestLoader.discover(TEST_DIR)
    logging.debug("{}测试开始{}".format("="*25,"="*25))
    with open(REPORT_FILE,"wb")as f:
        HTMLTestRunner(stream=f,
                       title=REPORT_FILE,
                       description=REPORT_DESCRIPTION).run(suite)
        logging.debug("{}测试结束{}".format("="*25,"="*25))


if __name__=="__main__":
    main()