# -*- coding: utf-8 -*-
__author__ = 'Fireln'
"""
    @auther : Fireln
    @time : 
"""
from getcase import getcasebase
from processParames import processParames232
import setting


class QaBusinessOne(getcasebase.GetCase):



    def getlen(self):

        return super().get_len_base()

    def getcase(self,i):
        pp = processParames232.processparames()

        return super().get_case_base(i,pp.getparames)



if __name__ == '__main__':
    casefilename = setting.casedirpath+setting.testname['2.3.2']
    g= QaBusinessOne(casefilename)
    for i in range(6):
        print(g.getcase(i))