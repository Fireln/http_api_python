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

    def getparames(self,parames):
        """
        Parames处理入口方法
        :param parames:
        :return:返回最终使用的Parames
        """
        self.parames = parames
        ak = isinstance(self.parames["changeactkey"],list)
        jk = isinstance(self.parames["fixedactkey"],list)
        rn = isinstance(self.parames["RandomNum"],list)
        if  ak:
            self.parames = self.process_Jsonkey('changeact')
        if  jk:
            self.parames = self.process_Jsonkey('fixedact')
        if  rn:
            self.parames = self.process_RandomNum()
        return self.parames['Parames']


    def process_Jsonkey(self,type):
        """
        1.只做了response是一层结构的取值
        2.根据具体需求进行重写
        :param type: 获取参数类型
                    1.changeact：上个接口response的返回结果
                    2.fixedact： 固定接口response的返回结果
                    3.每次调用根据传进来的type取到相应的值
        :return:
        """
        requestkey = self.parames[type] #request中所使用的key,用例中用type作为key
        responsekey = self.parames[type+'key'] #使用response中的key,用例中用type + key(这里是指字符串key)做为key
        defaultvalue = self.parames[type+'default']
        jsondata = self.pj.readJson()
        parame = self.parames['Parames']
        if jsondata[type] == '':
            for key1,key2 in zip(requestkey,defaultvalue):
                parame[key1] = key2
                return self.parames
        else:
            if isinstance(parame,str):
                for key in responsekey:
                    parame = jsondata[type]['Data'][key]
                return self.parames
            elif isinstance(parame,dict):
                for key1,key2 in zip(requestkey,responsekey):
                    parame[key1] = jsondata[type]['Data'][key2]
                return self.parames


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
















