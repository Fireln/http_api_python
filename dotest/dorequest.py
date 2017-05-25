import requests
import json

class HttpClent:

    def __init__(self):

        self. header = {
            "Accept":"application/json",
            "Content-Type":"application/json"
       }

    def do_get(self,url,body):
        """
            Get接口调用
            根据Parames类型确定传参方式
        """
        if len(body) == 0:
            response = requests.get(url=url,headers=self.header)
            return response
        else:
            response = requests.get(url=url,params=body,headers=self.header)
            return response

    def do_post(self,url,body):
        """
            Post接口调用
            根据Parames类型确定传参方式
        """
        if len(body) == 0:
            response = requests.post(url=url,headers=self.header)
            return response
        else:
            response = requests.post(url=url,json=body,headers=self.header)
            return response

    def do_put(self,url,body):

        if len(body) == 0:
            response = requests.put(url=url,headers=self.header)
            return response
        else:
            response = requests.put(url=url,json=body,headers = self.header)
            return response


    def do_delete(self,url,body):

        if len(body) == 0:
            response = requests.delete(url=url,headers=self.header)
            return response
        else:
            response = requests.delete(url=url,json=body,headers=self.header)
        #print(response_text.status_code)
        return response


    def run_request(self,host,type,parame,method):
        url = host + parame.get("path")
        body = parame.get("body")
        request = {
            'get':self.do_get,
            'post':self.do_post,
            'put':self.do_put,
            'delete':self.do_delete
        }
        if method.lower() in request.keys():
            if len(type) > 1:
                pass
            else:
                response = request[method.lower()](url,body)
                return response


if __name__ == '__main__':
    pass