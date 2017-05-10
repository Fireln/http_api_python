# -*- coding: utf-8 -*-
__author__ = 'Fireln'
"""
    @auther : Fireln
    @time : 
"""
import unittest
from comment import logging_class
import setting

class Test(unittest.TestCase):


    def testlog_building(self):
        logging = logging_class.Logging()
        logging.clear_log()
        logging.write_log(setting.log["INFO"],"test")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()