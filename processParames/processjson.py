import json
import os
import setting


class ProcessJson:
    """
        用于一个response内容被以后多个API使用
    """
    def openJson(self):
        jsonfilepath =  setting.actpath
        #dataprocess = dataprocess.Peocess()
        if os.path.exists(jsonfilepath) == False: #检查是否有json文件如果没有创建
            file = open(jsonfilepath,'w+')
            file.close()
            return self.openJson()
        else:
            jsonfile = open(jsonfilepath,'r+',encoding='utf-8')
            return jsonfile
    def readJson(self):
        """
            读取文件内容，输出Json格式
        """
        jf = self.openJson()
        default = {
            'lastact':'',
            'styact':''
        }
        try:
            str = jf.read()
            length = len(str)
            if length > 0:
                jsondata = json.loads(str)
                #print(jsondata)
                jf.close()
                return jsondata
            else:
                return default
        except Exception as e:
            print(e)


    def reresponse(self,response,writekey):
        """
        封装需要写入的值：
        1.调用self.readjson()获取原有数据
        2.写入本次结果
        :param response: 接口返回的response
        :param writekey: response.json()写入到的key
        :return: 返回本次需要写入的结果类型为dict
        """
        code = response.status_code
        dict = self.readJson()
        if code == 200 and writekey == 1:
            dict['styact'] = response.json()
            return dict
        elif code == 200 and writekey != 1:
            dict['lastact'] = response.json()
            return dict
        elif code != 200 and writekey == 1:
            dict['styact'] = ''
            return dict
        elif code != 200 and writekey != 1:
            dict['lastact'] = ''
            return dict

    def writeJson(self,response,writekey):
        """
        写如response保存文件
        1.调用self.rersponse()获得要写入的结果
        2.写入文件
        :param response: 接口返回结果
        :param writekey: 写入内容匹配键
        :return: None
        """

        dict = self.reresponse(response,writekey)

        try:
            jf = self.openJson()
            jf.truncate() #清除原有数据
            data = json.dumps(dict,indent=4)
            jf.write(data)
            jf.close()
        except Exception as e:
            print(__file__,'writeJson方法',e)


    def strToJson(self,str):
        """
        string转json方法
        :param str:
        :return:
        """
        try:
            jsondata = json.loads(str.replace('/n',''))
            return jsondata
        except Exception as e:
             print(__file__,'strToJson方法',e)
             return str








if __name__ == '__main__':
    print(__file__)
    a = ProcessJson()
    print(a.readJson())
