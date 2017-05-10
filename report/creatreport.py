# -*- coding: utf-8 -*-
__author__ = 'Fireln'
"""
    @auther : Fireln
    @time : 
"""
import xlsxwriter
from datetime import datetime
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


        #worksheet.merge_range('F4:F6', getcase['test_avg'], self.get_format_center(workbook))

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



if __name__ == '__main__':
    a = CreateReportModel()
    a.create_report()









