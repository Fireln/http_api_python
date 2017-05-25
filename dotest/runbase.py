from processParames import processjson
from dotest import dorequest
from comment import check,logging_class
from report.creatreport import CreateReportModel
import setting
class RunCase:

    def __init__(self):
        """
            初始化....
            Paramet,host:域名
        """
        self.summerysheetname = r'测试总况'
        self.detailssheetname = r'测试详情'
        self.check = check.Check()
        self.writejson = processjson.ProcessJson()
        self.createreportmodel = CreateReportModel()
        self.logging = logging_class.Logging()
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



    def runcase(self,length,function):
        """
            遍历执行测试用例接口
            Params，name:excel sheet名，即域名关键字
        """
        request = dorequest.HttpClent()
        try:
            for i in range(length):
                caseid,casename,host,method,parame,type,checkdata,ResponseSaveType = function(i)
                response = request.run_request(host,type,parame,method)
                if isinstance(response,str):
                    self.num['test_failed'] += 1
                    self.num['test_sum'] += 1
                    self.create_data(caseid,casename,host,parame.get("path"),parame,parame,response,'false')
                else:
                    resoult = self.check.runchek(response,checkdata)
                    if resoult.lower() == 'pass':
                        self.num['test_success'] += 1
                        self.num['test_sum'] += 1
                    else:
                        self.num['test_failed'] += 1
                        self.num['test_sum'] += 1
                    self.writejson.writeJson(response,ResponseSaveType)
                    self.logging.write_log(setting.log['INFO'],casename+parame.get("path"))
                    self.create_data(caseid,casename,"token",host,parame.get("path"),parame,checkdata,response.text,resoult)
        except Exception as e:
            self.logging.write_log(setting.log['ERROR'],e)






