# -*- coding: utf-8 -*-
__author__ = 'Fireln'
"""
    @auther : Fireln
    @time : 
"""
import unittest
import setting
from getcase import getcaseqa
class Test(unittest.TestCase):

    def test_qa(self):
        casefilename = setting.casedirpath+setting.testname['2.3.2']
        b = getcaseqa.QaBusinessOne(casefilename)
        b.get_len_base()
        b.getcase(1)



if __name__ == '__main__':
    unittest.main()