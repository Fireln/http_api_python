# -*- coding: utf-8 -*-
__author__ = 'Fireln'
"""
    @auther : Fireln
    @time :
"""
from connsql import connectmysql
import requests
conn = connectmysql.ConnMysql()
url = r'http://test.jishulink.com:8080/jishulink_test/coin/addCoin?userId=%s&coinNumber=1000&addReason=添加啊'
path = r"C:\Users\jiangfeilong\Desktop\apache-jmeter-3.1\myword\test.csv"
query = 'SELECT user_id FROM tbl_vw_user WHERE telephone = %s'



with open(path,'r') as r:
    while True:
        if r.readline():
            tel = r.readline(11)
            new_query = query % tel
            select_ret = conn.do_select(new_query,'jishulink-view-test')
            userid = select_ret[0]
            new_url = url % userid
            requests.post(new_url)
            print(new_url)
        else:
            break