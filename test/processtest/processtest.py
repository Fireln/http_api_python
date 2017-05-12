# -*- coding: utf-8 -*-
__author__ = 'Fireln'
"""
    @auther : Fireln
    @time : 
"""
import unittest
from processParames import processparamesbase
import setting

class ProcessTest(unittest.TestCase):

    parames= {"Parames":{
                    "parames":
                        {
                            "query": "?name=13783783183&password=111111",
                            "body": {},
                        },
                    "path": "/user/authenticate/name/%s/%d/%s",
                    "type": "path", #接口方法
                    "where": ["path"], #哪里需要用到参数
                    "usepath": ['lastactkey','styactkey','randomkey'], #参数去哪里找
                    "pathkey": [], #取出value用到的key路径
                    "usequery": [], #query里面是否用到参数，用到的是哪里的参数
                    "usebody": [], #body里是否用到参数用到的是哪里的参数
                    #"uselastact": False, #是否用到了上个接口的返回值
                    "lastactkey": ["ret","profile","male"], #取出value用到的key路径
                    #"usestyact":  False, #是否用到了固定接口的返回值
                    "styactkey": ["ret","profile","age"], #取出value用到的key路径
                    #"userandom": False, #参数中是否有用到随机数
                    "randomkey": []
                  }}
    pp = processparamesbase.Processing(parames = parames,lastactkey=["ret","profile","male"],randomkey=['random'],styactkey=["ret","profile","male"])

    def test_getparames(self):

        print(self.pp.getparames(parames=self.parames))

    def test_path(self):

        value = self.pp.process_path(["lastactkey","styactkey","randomkey"])
        print(value)

    def test_query(self):

        pass
    def test_body(self):
        pass


    def test_Jsonkey(self):
        value1 = self.pp.process_Jsonkey(["ret","profile","age"],"lastact")
        value2 = self.pp.process_Jsonkey(["ret","profile","age"],"styact")
        assert value1 == 10 and value2 == 10



    def test_value(self):
        l = ["Parames","query"]
        value  = self.pp.get_value(self.parames,l)
        assert value == "?name=13783783183&password=111111"




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(ProcessTest('test_getparames'))
    runner = unittest.TextTestRunner()
    runner.run(suite)