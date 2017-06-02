# -*- coding: utf-8 -*-
__author__ = 'Fireln'
"""
    @auther : Fireln
    @time : 
"""

import os
import yaml
from processParames import processparamesbase

class GetCase:

    def __init__(self,casefilepath):
        self.pparames = processparamesbase.Processing()
        self.casefilepath = casefilepath


    @property
    def openfile(self):
        """
        :return:用例配置文件
        """
        try:
            casefile = open(self.casefilepath,encoding='utf-8')
            return casefile
        except Exception as e:
            print(__file__,"openfile函数出错",e)


    def getcaseinfo(self,name):
        """
        :return:用例信息
        """
        file = self.openfile
        setting = yaml.load(file)
        caseinfo = setting[name]
        file.close()
        return caseinfo



    def get_len_base(self,name):
        """
        :return:用例条目
        """
        caseinfo = self.getcaseinfo(name)
        length = len(caseinfo)
        return length

    def get_case_base(self,i,function,name):
        """
        获取用例底层方法
        :param i:
        :param function:子类处理用例的方法
        :return:
        """
        caseinfo = self.getcaseinfo(name)
        case = caseinfo[i]
        caseid = case['caseid']
        casename = case['casename']
        host = case['host']
        method = case['method']
        parames = case['parames']
        type = case['type']
        checkdata = case['checkdata']
        ResponseSaveType = case['ResponseSaveType']
        parame = function(parames)
        #print(caseid,casename,host,api,method,parames,checkdata,ResponseSaveType)
        return caseid,casename,host,method,parame,type,checkdata,ResponseSaveType
