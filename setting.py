# -*- coding: utf-8 -*-
__author__ = 'Fireln'
"""
    @auther : Fireln
    @time : 
"""
import os

casedirpath = os.path.split(os.path.realpath(__file__))[0]+r'\casedata'
reportdirpath = os.path.split(os.path.realpath(__file__))[0]+r'\report'
actpath = os.path.split(os.path.realpath(__file__))[0]+r'\processParames\act.json'


testname = {
    'qa':r'\qacase.yaml',
    'test':r'\testcase.yaml'
}

reportname = {

    '2.3.2': '\APITest2.3.2.xlsx'
}

log = {
    "log_conf":os.path.split(os.path.realpath(__file__))[0]+r'\applogconfig.ini',
    "log":os.path.split(os.path.realpath(__file__))[0]+r'\log.log',
    'CRITICAL':'CRITICAL',
    'ERROR':'ERROR',
    'WARNING':'WARNING',
    'INFO':'INFO',
    'DEBUG':'DEBUG'
}


database = {
    'host':'120.55.131.33',
    'name':'jishulink_test',
    'pwd':'jishulink1194',
    'port':3306
}



