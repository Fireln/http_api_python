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
        casefilename = setting.casedirpath+setting.testname['qa']
        b = getcaseqa.QaBusinessOne(casefilename)
        b.get_len_base()
        print(b.getcase(0))



if __name__ == '__main__':
    unittest.main()