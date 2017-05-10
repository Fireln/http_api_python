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

print(casedirpath)
testname = {
    '2.3.2':r'\testcase.yaml'
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



