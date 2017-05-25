# -*- coding: utf-8 -*-
__author__ = 'Fireln'
"""
    @auther : Fireln
    @time : 
"""

from comment import tojson
from processParames import processjson
from datetime import datetime
from comment import userinfo
import time


class Processing:
    """
        测试参数Params处理基类
    """
    def __init__(self,parames = None,lastactkey=None,styactkey=None,randomkey=None):
        self.pj = processjson.ProcessJson()
        self.userinfo = userinfo.GetUserInfo()
        self.tojson = tojson.ToJson()
        self.parames = parames
        self.pathkey = []
        self.lastactkey = lastactkey
        self.styactkey = styactkey
        self.randomkey = randomkey


    def getparames(self,parames):
        """
        哪里需要参数并分发到对应的处理方法
        :param parames:
        :return:返回最终使用的Parames
        """
        self.parames = parames
        self.bodykey = self.parames.get('bodykey')
        self.lastactkey = self.parames.get('lastactkey')
        self.styactkey = self.parames.get('styactkey')
        self.randomkey = self.parames.get('randomkey')
        where = self.parames.get("where")
        type = {
            "path":self.process_path,
            "body":self.procss_body
        }
        if len(where) != 0:
            for i in where:
                type[i[0]](i)
            return self.parames["Parames"]
        else:
            return self.parames["Parames"]


    def use(self,num):
        """
        组装参数
        :param usepath:
        :return:
        """
        value = []
        process = {
            "lastactkey": self.process_Jsonkey,
            "styactkey": self.process_Jsonkey,
            "randomkey": self.process_RandomNum,
            "userid": self.userinfo.login
        }
        data = num[1:]
        for i in data:
            value1 = process[i](i)
            value.append(value1)
        return value

    def process_path(self,num):
        """
        path处理方法
        :return:
        """
        path = self.parames.get('Parames').get("path")
        value = self.use(num)
        newpath = path % tuple(value)
        self.parames["Parames"]["path"] = newpath
        return self.parames.get('Parames').get("path")



    def procss_body(self,body):

        return


    def process_Jsonkey(self,type):


        jsondata = self.pj.readJson() #拿出结果
        lastact = jsondata.get('lastact')
        styact = jsondata.get('styact')
        if type == "lastact":
            return self.get_value(lastact,self.lastactkey)
        else:
            return self.get_value(styact,self.styactkey)



    def process_RandomNum(self):
        """
        1.时间戳生成唯一标识方法
        2.只生成了时刻点
        3.未考虑长度
        4.根据具体需求进行重写
        :param parames:
        :return:
        """
        #for key in self.parames['RandomNum']:
        #    value = str(datetime.now())
        #    time.sleep(0.001) #代码执行太快导致value值一样
        return str(datetime.now())


    def get_value(self,data,keylist):
        """

        :param data: 从中获取value的json对象
        :param keylist: value的key路径
        :return:
        """

        if len(keylist) < 1:
            return data
        else:
            da = data.get(keylist[0])
            tt = keylist[1:]  #用切片的原因是因为pop后如果只有一个元素的话就会变成String类型
            return self.get_value(da,tt)














