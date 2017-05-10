# -*- coding: utf-8 -*-
__author__ = 'Fireln'
"""
    @auther : Fireln
    @time : 
"""
import pymysql
from xml.dom import minidom
import os

class ConnMysql():

    def __init__(self):
        #self.host = host
        conf = minidom.parse(r'F:\DiDiXLAPITEST\testdata\conf')
        self.host = conf.getElementsByTagName("host")[0].firstChild.data
        self.port = int(conf.getElementsByTagName("port")[0].firstChild.data)
        self.user = conf.getElementsByTagName("user")[0].firstChild.data
        self.passwd = conf.getElementsByTagName("passwd")[0].firstChild.data


    def createconn(self,database):
        try:
            conn = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,database=database)
            cur = conn.cursor()
            return cur,conn
        except Exception as e:
            print('数据库连接错误',e)
    def do_select(self,query,database):
        try:
            cur,conn = self.createconn(database)
            cur.execute(query)
            self.processres(cur)
            self.closeconn(cur,conn)
        except Exception as e:
            print('查询命令错误',e)
    def do_update(self,query,database):
        try:
            cur,conn = self.createconn(database)
            cur.execute(query)
            self.processres(cur)
            self.closeconn(cur,conn)
        except Exception as e:
            print('查询命令错误',e)
    def do_insert(self,query,database):
        try:
            cur,conn = self.createconn(database)
            cur.execute(query)
            self.processres(cur)
            self.closeconn(cur,conn)
        except Exception as e:
            print('查询命令错误',e)
    def do_delete(self,query,database):
        try:
            cur,conn = self.createconn(database)
            cur.execute(query)
            self.processres(cur)
            self.closeconn(cur,conn)
        except Exception as e:
            print('查询命令错误',e)
    def processres(self,cur):
        rows = cur.fetchall()
        for i in rows:
            print(i)
    def closeconn(self,cur,conn):
        cur.close()
        conn.close()


if __name__ == '__main__':
    con = ConnMysql()
    con.do_select(r'SELECT * from get WHERE id = 222','test')