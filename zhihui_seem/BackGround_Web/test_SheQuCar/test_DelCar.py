import json
import requests
import unittest
import pymysql
from lib.db_conn import query_db,del_db,get_conn
import time


class TestShequCar(unittest.main):
    def test_ShequCar_Del(self):
        url=""