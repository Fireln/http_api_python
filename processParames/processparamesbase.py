# -*- coding: utf-8 -*-
__author__ = 'Fireln'
"""
    @auther : Fireln
    @time : 
"""

from comment import tojson
from processParames import processjson
from datetime import datetime
import time


class Processing:
    """
        测试参数Params处理基类
    """
    def __init__(self):
        self.pj = processjson.ProcessJson()
        self.tojson = tojson.ToJson()
        self.parames = {}
        self.pathkey = []
        self.lastactkey = []
        self.styactkey = []
        self.randomkey = []


    def getparames(self,parames):
        """
        Parames处理入口方法
        :param parames:
        :return:返回最终使用的Parames
        """
        self.parames = parames["Parames"]
        self.pathkey = self.parames.get('pathkey')
        self.lastactkey = self.parames.get('lastactkey')
        self.styactkey = self.parames.get('styactkey')
        self.randomkey = self.parames.get('randomkey')
        usepath = self.parames.get('usepath')
        usequery = self.parames.get('usequery')
        usebody = self.parames.get('usebody')
        type = {
            "path":self.process_path,
            "query":self.process_query,
            "body":self.procss_body
        }
        for i in self.parames["Type"]:
            type[i](usepath)
        return self.parames


    def use(self,usepath):

        value = []
        process = {
            "lastactkey": self.process_Jsonkey,
            "styactkey": self.process_Jsonkey,
            "randomkey": self.process_RandomNum
        }
        if "lastactkey" in usepath:
            value1 = process.get("process")(self.lastactkey,"lastact")
            value.append(value1)
        if "styactkey" in usepath:
            value2 = process.get("process")(self.styactkey,"styact")
            value.append(value2)
        if "randomkey" in usepath:
            value3 = process.get("process")(self.randomkey)
            value.append(value3)


        return self.parames['Parames']

    def process_path(self,usepath):
        if usepath:
           pass
        else:
            path = self.parames.get('path')
            value = self.use(usepath)
            newpath = path % value
            self.parames["path"] = newpath


    def process_query(self,query,):

        return


    def procss_body(self,body):

        return


    def process_Jsonkey(self,keylist,type):


        jsondata = self.pj.readJson() #拿出结果
        lastact = jsondata.get('lastact')
        styact = jsondata.get('styact')
        if type == "lastact":
            return self.get_value(lastact,keylist)
        else:
            return self.get_value(styact,keylist)



    def process_RandomNum(self):
        """
        1.时间戳生成唯一标识方法
        2.只生成了时刻点
        3.未考虑长度
        4.根据具体需求进行重写
        :param parames:
        :return:
        """
        for key in self.parames['RandomNum']:
            self.parames['Parames'][key] = str(datetime.now())
            time.sleep(0.001) #代码执行太快导致value值一样
        return self.parames


    def get_value(self,data,keylist):

        if len(keylist) == 0:
            return data
        else:
            da = data.get(keylist[0])
            tt = keylist[1:]  #用切片的原因是因为pop后如果只有一个元素的话就会变成String类型
            return self.get_value(da,tt)














