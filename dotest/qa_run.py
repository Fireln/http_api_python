# -*- coding: utf-8 -*-
__author__ = 'Fireln'
"""
    @auther : Fireln
    @time : 
"""
import setting
from dotest import runbase
from getcase import getcaseqa


class Run(runbase.RunCase):

    def qa_run(self):
        casefilename = setting.casedirpath + setting.testname['qa']
        getcase = getcaseqa.QaBusinessOne(casefilename)
        function = getcase.getcase
        length = getcase.getlen()
        self.runcase(length,function)



    def creatreport(self):
        self.createreportmodel.create_report(self.num,self.data)



if __name__ == '__main__':
    from comment import logging_class
    Logging = logging_class.Logging()
    Logging.clear_log()#清空日志文件
    r=Run()
    r.qa_run()
    r.creatreport()

