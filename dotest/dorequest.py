import requests
import json

class HttpClent:

    def __init__(self,token):
        """
            初始化....
            Parames,host:域名
            Parames,api:接口url
            Parames,params:path\query参数
            Parames,token:有效token
        """
        self.token = token
        self. header = {
            "Accept":"application/json",
            "Content-Type":"application/json",
            "Authorization":'Bearer '+"%s" % self.token,
            "Device":"android"
       }
        self.runrequest = {
            'get':self.doGet,
            'post':self.doPost,
            'put':self.doPut,
            'delete':self.doDelete
        }
    def doGet(self,url,params):
        """
            Get接口调用
            根据Parames类型确定传参方式
        """
        try:
            if isinstance(params,dict):
                response = requests.get(url=url,params=params,headers=self.header)
                return response
            elif isinstance(params,str) and params != '':
                response = requests.get(url=url+'/'+params,headers=self. header)
                return response
            else:
                response = requests.get(url=url,headers=self. header)
                return response
        except Exception as e:
            assert "doGet运行出错",e
    def doPost(self,url,params):
        """
            Post接口调用
            根据Parames类型确定传参方式
        """
        try:
            if isinstance(params,str) and params not in 'None,x':
                response = requests.post(url=url+'/'+params,json=params,headers=self. header)
                return response
            elif isinstance(params,dict):
                response = requests.post(url=url,json=params,headers=self. header)
                return response
            else:
                response = requests.post(url=url,json=params,headers=self. header)
                return response
        except Exception as e:
            return "doPost运行出错",e

    def doPut(self,url,params):
        try:
            if isinstance(params,str) and params == 'path':
                response = requests.put(url=url+'/' + params,headers=self.header)
                return response
            elif isinstance(params,dict):
                response = requests.put(url=url,json=params,headers = self.header)
                return response
            elif isinstance(params,str) and params == '':
                response = requests.put(url=url,headers = self.header)
                return response
            else:
                return "缺少参数，请检查参数"
        except Exception as e:
            return "doPut运行出错",e
    def doDelete(self,url,params):
        try:
            response = requests.delete(url=url,params=params,headers=self.header)
            #print(responsetext.status_code)
            return response
        except Exception as e:
            return "doDelete运行出错",e

    def runRespuest(self,Host, API, Parames,Method):
        url = Host + API
        if Method.lower() in self.runrequest.keys():
            response = self.runrequest[Method.lower()](url,Parames)
            return response


if __name__ == '__main__':
    pass