import json
class Check():
    """
        response结果检查类
    """
    def __init__(self):

        self.passres = 'Pass'
        self.falseres = 'False'
        self.checkrule = {
            'int' : self.check_int,
            'key' : self.check_Key,
            'keyvalue':self.check_keyvalue,
            'bool':self.check_bool

        }

    def check_int(self,actualRes=None,checkdata=None,*args,**kwargs):

        if int(actualRes) == int(checkdata['Data']):
            return self.passres
        else:
            return self.falseres
    def check_bool(self,actualRes=None,checkdata=None,*args,**kwargs):

        if actualRes:
            return self.passres
        else:
            return self.falseres


    def check_Key(self,actualRes=None,checkkeylist=None,*args,**kwargs):
        """
            检查response中的key，遍历全部的key
        """
        self.reslist = []
        self.wrongkey = []
        for key in checkkeylist:
            if key in actualRes.keys():
                self.reslist.append(self.passres)
            else:
                self.reslist.append(self.falseres)
                self.wrongkey.append(key)
        if self.falseres in self.reslist:
            return self.falseres,'reponse缺少key:%s' % self.wrongkey
        else:
            return self.passres



    def check_keyvalue(self,actualRes=None,checkdata=None,*args,**kwargs):
        """
            检查response返回的key-value,一级对象
        """
        self.reslist = []
        self.wrongkey = []
        for i in checkdata.items():
            if i in actualRes.items():
                self.reslist.append(self.passres)
            else:
                self.reslist.append(self.falseres)
                self.wrongkey.append(i)
        if self.falseres in self.reslist:
            return self.falseres + ',接口返回的key-value错误 %s' % self.wrongkey
        else:
            return self.passres


    def runchek(self,response,checkdata=None):
        """
            check入口函数
        """
        code = response.status_code
        if code == 200:
            ActualRes = response.json()
            checktype = checkdata['checktype']
            checkdata = checkdata['checkdata']
            actualRes = ActualRes['ret']
            if checktype == 'code':
                rc = ActualRes.get("rc")
                if rc == 0:
                    return self.passres
            if isinstance(checkdata,dict):
                checkkeylist = checkdata.keys()
            else:
                checkkeylist = checkdata
            #print(self.checkrule.keys())
            if checktype in self.checkrule.keys():
                res = self.checkrule[checktype.lower()](actualRes=actualRes,checkdata=checkdata,checkkeylist=checkkeylist)
                return res
        else:
            return self.falseres
