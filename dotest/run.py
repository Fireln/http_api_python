# -*- coding: utf-8 -*-
__author__ = 'Fireln'
"""
    @auther : Fireln
    @time : 
"""
import setting
from dotest import runcase
from getcase import getcaseqa


class Run(runcase.RunCase):

    def runcase232(self):
        casefilename = setting.casedirpath + setting.testname['2.3.2']
        getcase = getcaseqa.GetCase(casefilename)
        function = getcase.getcase232
        length = getcase.getlen()
        self.runcase(length,function)

    def runcase231(self):
        casefilename = setting.casedirpath + setting.testname['2.3.2']
        getcase = getcaseqa.GetCase(casefilename)
        function = getcase.getcase232
        length = getcase.getlen()
        self.runcase(length,function)



    def creatreport(self):

        self.createreportmodel.create_report(self.num,self.data)



if __name__ == '__main__':
    r=Run()
    r.runcase232()
    r.runcase231()
    r.creatreport()

