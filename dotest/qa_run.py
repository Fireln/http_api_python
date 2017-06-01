# -*- coding: utf-8 -*-
__author__ = 'Fireln'
"""
    @auther : Fireln
    @time : 
"""
import setting
from dotest import runbase
from getcase import getcaseqa


class Run:

    def __init__(self):

        self.countres = {'info':[]}
        self.num  =  {
            'test_success':0,
            'test_failed':0,
            'test_sum': 0,
        }
    def qa_run(self):
        run = runbase.RunCase()
        casefilename = setting.casedirpath + setting.testname['qa']
        getcase = getcaseqa.QaBusinessOne(casefilename)
        function = getcase.getcase
        length = getcase.getlen()
        data = run.runcase(length,function)
        self.process_data(data.get("info"),run.num)


    def qarun(self):
        run = runbase.RunCase()
        casefilename = setting.casedirpath + setting.testname['qa']
        getcase = getcaseqa.QaBusinessOne(casefilename)
        function = getcase.getcase
        length = getcase.getlen()
        data = run.runcase(length,function)
        self.process_data(data.get("info"),run.num)

    def process_data(self,info,num):
        self.countres["info"] += info
        self.num["test_success"] += num["test_success"]
        self.num["test_failed"] += num["test_failed"]
        self.num["test_sum"] += num["test_sum"]

    def creatreport(self):
        run = runbase.RunCase()
        run.createreportmodel.create_report(self.num,self.countres)



if __name__ == '__main__':
    from comment import logging_class
    Logging = logging_class.Logging()
    Logging.clear_log()#清空日志文件
    r=Run()
    r.qa_run()
    r.qarun()
    r.creatreport()

