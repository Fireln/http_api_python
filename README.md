
# 基于业务的API自动化测试方案

## 1.用例设计详解

用例采用yaml文件编写，如下：

```
version: 
author: 
createtime: 
setting:
    constenthost: &chost
        host:  http://consultant.test.didixl.com
    doctorhost: &dhost
        host:  http://doctor.test.didixl.com

caseinfo:
    -
        caseid: 1
        casename: "设置量表"
        <<: *chost
        api: /api/Assessment
        method: post
        parames: {
                    "Parames": [
                        {
                            "UserId": 187,
                            "AssessmentId": 2,
                            "AssessmentKind": 2,
                            "AssessmentName": "量表名称",
                            "AssessmentUrl": "www.量表Url.com",
                            "Mode": 1
                        }
                    ],
                      "Type": "body",
                      "changeact": [],
                      "changeactkey": [],
                      "fixedact":  [],
                      "fixedactkey": [],
                      "RandomNum": []
                  }
        checkdata: {
            "checktype": "code",
            "checkdata":
        }
        ResponseSaveType: 0
```
下面来阐述每个字段的作用和意义：
* caseId: 
* casename: 
* host: 
* api: 
* method: 接口使用方法
* parames:
  * Parames: 调用接口使用的参数
  * Type：传参类型(path、query、body),可能个别接口会涉及到多种传参方式，可以扩展成list
  * changeact：接口入参key(使用上个接口)
  * changeactkey：获取response中值的key(这个设计用于下个接口需使用上个接口response中的值，注意changeact和changeactkey两个list的排序)
  * fixedact：接口入参key(使用固定接口)
  * fixedactkey：获取response中值的key(这个设计用于下个接口需使用固定接口response中的值，注意changeact和changeactkey两个list的排序)
  * RandomNum：入参中唯一字段的key
* checkdata：response检查
  * checktype：检查类型(code,bool,key,keyvalue)
  * checkdata: 预期结果
* ResponseSaveType：结果保存类型(1:fixed类型保存到业务完成，用于本次业务中以后接口需要其中的值；0：change类型每次调用接口都会改变，用于下个接口需要其中的值)

## 2.获取用例

基类代码如下：
```
class GetCase:

    def __init__(self,casefilepath):
        self.pparames = processparamesbase.Processing()
        self.casefilepath = casefilepath


    @property
    def openfile(self):
        """
        :return:用例配置文件
        """
        try:
            casefile = open(self.casefilepath,encoding='utf-8')
            return casefile
        except Exception as e:
            print(__file__,"openfile函数出错",e)

    @property
    def getcaseinfo(self):
        """
        :return:用例信息
        """
        file = self.openfile
        setting = yaml.load(file)
        caseinfo = setting['caseinfo']
        file.close()
        return caseinfo



    def getlen(self):
        """
        :return:用例条目
        """
        caseinfo = self.getcaseinfo
        length = len(caseinfo)
        return length

    def getcase(self,i,function):
        """
        获取用例底层方法
        :param i:
        :param function:子类处理用例的方法
        :return:
        """
        caseinfo = self.getcaseinfo
        case = caseinfo[i]
        caseid = case['caseid']
        casename = case['casename']
        host = case['host']
        api = case['api']
        method = case['method']
        parames = case['parames']
        checkdata = case['checkdata']
        ResponseSaveType = case['ResponseSaveType']
        parame = function(parames)
        #print(caseid,casename,host,api,method,parames,checkdata,ResponseSaveType)
        return caseid,casename,host,api,method,parame,checkdata,ResponseSaveType
```



基类中用到了接口入参处理方法，下面介绍参数处理模块，基类代码如下：

```
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
```
入参处理时用到的json操作类代码如下：
```
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
            'changeact':'',
            'fixedact':''
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
            dict['fixedact'] = response.json()
            return dict
        elif code == 200 and writekey != 1:
            dict['changeact'] = response.json()
            return dict
        elif code != 200 and writekey == 1:
            dict['fixedact'] = ''
            return dict
        elif code != 200 and writekey != 1:
            dict['changeact'] = ''
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
            data = json.dumps(dict)
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
```
注意接口入参处理需要其他接口数据的处理基类中只考虑了respose的单层架构，我准备遇到后看情况是把参数处理方法写在基类还是在子类。

# 3.接口调用

参数全部取到后就要进行接口调用了，请求处理类代码如下：

```
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
```

# 4.response检查

代码如下：
```
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
            actualRes = ActualRes['Data']
            if checktype == 'code':
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
```

这个检查类型不全面，遇到什么补什么，还是以基类派生类的方法管理

# 5.报告生成

这个是用的testhome以为朋友分享的，我修改了下，【原

文链结】

代码如下：

```
class Method():

    def get_format(self,wd,option = {}):

        return wd.add_format(option)
    # 设置居中
    def get_format_center(self,wd,num=1):

        return wd.add_format({'align': 'center','valign': 'vcenter','border':num})


    def set_border_(self,wd, num=1):

        return wd.add_format({}).set_border(num)


    def _write_center(self,worksheet, cl, data, wd):

        return worksheet.write(cl, data, self.get_format_center(wd))

    def pie(self,workbook,worksheet):
        chart1 = workbook.add_chart({'type': 'pie'})
        chart1.add_series({
        'name':       '接口测试统计',
        'categories':'=测试总况!$D$4:$D$5',
        'values':    '=测试总况!$E$4:$E$5',
        })
        chart1.set_title({'name': '接口测试统计'})
        chart1.set_style(10)
        worksheet.insert_chart('A9', chart1, {'x_offset': 25, 'y_offset': 10})

class CreateReportModel(Method):

    def create_summary(self,workbook,worksheet,data):
        # 设置列行的宽高
        worksheet.set_column("A:A", 15)
        worksheet.set_column("B:B", 20)
        worksheet.set_column("C:C", 20)
        worksheet.set_column("D:D", 20)
        worksheet.set_column("E:E", 20)
        worksheet.set_column("F:F", 20)

        worksheet.set_row(1, 30)
        worksheet.set_row(2, 30)
        worksheet.set_row(3, 30)
        worksheet.set_row(4, 30)
        worksheet.set_row(5, 30)

        # worksheet.set_row(0, 200)

        define_format_H1 = self.get_format(workbook,{'bold': True, 'font_size': 18})
        define_format_H2 = self.get_format(workbook,{'bold': True, 'font_size': 14})
        define_format_H1.set_border(1)

        define_format_H2.set_border(1)
        define_format_H1.set_align("center")
        define_format_H2.set_align("center")
        define_format_H2.set_bg_color("blue")
        define_format_H2.set_color("#ffffff")
        # Create a new Chart object.

        worksheet.merge_range('A1:F1', '测试报告总概况', define_format_H1)
        worksheet.merge_range('A2:F2', '测试概括', define_format_H2)
        worksheet.merge_range('A3:A6', '这里放图片', self.get_format_center(workbook))

        self._write_center(worksheet, "B3", '项目名称', workbook)
        self._write_center(worksheet, "B4", '接口版本', workbook)
        self._write_center(worksheet, "B5", '脚本语言', workbook)
        self._write_center(worksheet, "B6", '测试网络', workbook)



        self._write_center(worksheet, "C3", data['test_name'], workbook)
        self._write_center(worksheet, "C4", data['test_version'], workbook)
        self._write_center(worksheet, "C5", data['test_pl'], workbook)
        self._write_center(worksheet, "C6", data['test_net'], workbook)



        self._write_center(worksheet, "D3", "接口总数", workbook)
        self._write_center(worksheet, "D4", "通过总数", workbook)
        self._write_center(worksheet, "D5", "失败总数", workbook)
        self._write_center(worksheet, "D6", "测试日期", workbook)
        self._write_center(worksheet, "E3", data['test_sum'], workbook)
        self._write_center(worksheet, "E4", data['test_success'], workbook)
        self._write_center(worksheet, "E5", data['test_failed'], workbook)
        self._write_center(worksheet, "E6", data['test_date'], workbook)
        self._write_center(worksheet, "F3", "通过率", workbook)
        avg = str(data['test_success']/data['test_sum']*100)[0:4]+'%'
        worksheet.merge_range('F4:F6', avg, self.get_format_center(workbook))


        #worksheet.merge_range('F4:F6', data['test_avg'], self.get_format_center(workbook))

    def create_details(self,workbook,worksheet,data):
        # 设置列行的宽高
        worksheet.set_column("A:A", 10)
        worksheet.set_column("B:B", 20)
        worksheet.set_column("F:F", 20)
        worksheet.set_column("C:C", 20)
        worksheet.set_column("D:D", 25)
        worksheet.set_column("E:E", 30)
        worksheet.set_column("F:F", 30)
        worksheet.set_column("G:G", 30)
        worksheet.set_column("H:H", 30)
        worksheet.set_column("I:I", 0)
        worksheet.set_row(0, 35)
        worksheet.set_row(1, 30)

        worksheet.merge_range('A1:H1', '测试详情', self.get_format(workbook, {'bold': True, 'font_size': 18 ,'align': 'center','valign': 'vcenter','bg_color': 'blue', 'font_color': '#ffffff'}))
        self._write_center(worksheet, "A2", '用例ID', workbook)
        self._write_center(worksheet, "B2", '接口名称', workbook)
        self._write_center(worksheet, "C2", 'token', workbook)
        self._write_center(worksheet, "D2", 'URL', workbook)
        self._write_center(worksheet, "E2", '参数', workbook)
        self._write_center(worksheet, "F2", '预期值', workbook)
        self._write_center(worksheet, "G2", '实际值', workbook)
        self._write_center(worksheet, "H2", '测试结果', workbook)
        for i,item in zip(range(len(data["info"])),data["info"]):
            worksheet.set_row(i+2, 30)
            self._write_center(worksheet, "A"+str(i+3), item["caseid"], workbook)
            self._write_center(worksheet, "B"+str(i+3), item["casename"], workbook)
            self._write_center(worksheet, "C"+str(i+3), item["token"], workbook)
            self._write_center(worksheet, "D"+str(i+3), item["url"], workbook)
            self._write_center(worksheet, "E"+str(i+3), str(item["parames"]), workbook)
            self._write_center(worksheet, "F"+str(i+3), str(item["ext"]), workbook)
            self._write_center(worksheet, "G"+str(i+3), str(item["act"]), workbook)
            if item["resoult"] == 'Pass':
                self._write_center(worksheet, "H"+str(i+3), item["resoult"], workbook)
            else:
                worksheet.merge_range('H%s:I%s'%(str(i+3),str(i+3)), item["resoult"], self.get_format(workbook, {'align': 'center','valign': 'vcenter','bg_color': 'red', 'font_color': '#ffffff'}))


    def create_report(self,num,data):
        temp = str(datetime.now())[0:16]
        numsummary = {"test_name": "的的心理", "test_version": "v2.0.8", "test_pl": "android", "test_net": "wifi",
             "test_date": temp }
        numsummary = dict(numsummary,**num)
        workbook = xlsxwriter.Workbook('DD_API_REPORT.xlsx')
        worksheet1 = workbook.add_worksheet('测试总况')
        worksheet2 = workbook.add_worksheet('测试详情')
        self.create_summary(workbook,worksheet1,numsummary)
        self.create_details(workbook,worksheet2,data)
        self.pie(workbook,worksheet1)
        workbook.close()
```

# 6.测试集成类

代码如下：
```
class RunCase:

    def __init__(self):
        """
            初始化....
            Paramet,host:域名
        """
        self.reportpath = setting.reportdirpath + setting.reportname['2.3.2']
        self.summerysheetname = r'测试总况'
        self.detailssheetname = r'测试详情'
        self.check = check.Check()
        self.login = gettoken.GetToken().login()
        self.writejson = processjson.ProcessJson()
        #self.report = creatreport.write_report()
        self.createreportmodel = CreateReportModel()
        self.num =  {
            'test_success':0,
            'test_failed':0,
            'test_sum': 0,
        }
        self.data = {'info':[]}


    def create_data(self,*args):
        nowdata = {'caseid': args[0],'casename': args[1],'token': args[2],'url': args[3]+args[4],'parames': args[5],
                               'ext': args[6],'act': args[7],'resoult': args[8]}
        self.data['info'].append(nowdata)


    def runcase(self,name):
        """
            遍历执行测试用例接口
            Params，name:excel sheet名，即域名关键字
        """
        casefilename = setting.casedirpath + setting.testname['2.3.2']
        database = getcase232.GetCase(casefilename)
        length = database.getlen()
        token = self.login
        request = dorequest.HttpClent(token)

        try:
            for i in range(length):
                caseid,casename,host,api,method,parame,checkdata,ResponseSaveType = database.getcase232(i)
                response = request.runRespuest(host, api, parame,method)
                if isinstance(response,str):
                    self.num['test_failed'] += 1
                    self.num['test_sum'] += 1
                    self.create_data(caseid,casename,token,host,api,parame,parame,response,'false')
                else:
                    resoult = self.check.runchek(response,checkdata)
                    if resoult.lower() == 'pass':
                        self.num['test_success'] += 1
                        self.num['test_sum'] += 1
                    else:
                        self.num['test_failed'] += 1
                        self.num['test_sum'] += 1
                    self.writejson.writeJson(response,ResponseSaveType)
                    self.create_data(caseid,casename,token,host,api,parame,checkdata,response.text,resoult)
            self.createreportmodel.create_report(self.num,self.data)
        except Exception as e:
            print("run运行错误",e)
```

