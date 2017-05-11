# -*- coding: utf-8 -*-
__author__ = 'Fireln'
"""
    @auther : Fireln
    @time : 
"""
import unittest
from comment import logging_class,userinfo
import setting

class CommentTest(unittest.TestCase):


    def test_logging(self):
        logging = logging_class.Logging()
        logging.clear_log()
        logging.write_log(setting.log["INFO"],"test")

    def test_userinfo(self):
        get_user_info = userinfo.GetUserInfo()
        r = get_user_info.login()
        print(r)



    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(CommentTest('test_userinfo'))
        suite.addTest(CommentTest('test_logging'))
        return suite


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(CommentTest('test_userinfo'))
    runner = unittest.TextTestRunner()
    runner.run(suite)