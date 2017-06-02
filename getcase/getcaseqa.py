# -*- coding: utf-8 -*-
__author__ = 'Fireln'
"""
    @auther : Fireln
    @time : 
"""
from getcase import getcasebase
from processParames import ppqa
import setting

#进入问答首页
class IntoQA(getcasebase.GetCase):

    def getlen(self):

        return super().get_len_base('intoqa')

    def getcase(self,i):
        pp = ppqa.processparames()

        return super().get_case_base(i,pp.getparames,'intoqa')

#发布悬赏问答
class PublishQA(getcasebase.GetCase):

    def getlen(self):

        return super().get_len_base('publishqa')

    def getcase(self,i):
        pp = ppqa.processparames()

        return super().get_case_base(i,pp.getparames,'publishqa')



if __name__ == '__main__':
    casefilename = setting.casedirpath+setting.testname['qa']
    g= PublishQA(casefilename)
    print(g.getcase(0))