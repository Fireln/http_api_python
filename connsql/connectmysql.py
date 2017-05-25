# -*- coding: utf-8 -*-
__author__ = 'Fireln'
"""
    @auther : Fireln
    @time : 
"""
import pymysql
from xml.dom import minidom
import setting

class ConnMysql():

    def __init__(self):
        #self.host = host
        self.host = setting.database.get("host")
        self.port = setting.database.get("port")
        self.user = setting.database.get("name")
        self.passwd = setting.database.get("pwd")


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
            ret = self.processres(cur)
            self.closeconn(cur,conn)
            return ret
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
            return i
    def closeconn(self,cur,conn):
        cur.close()
        conn.close()


if __name__ == '__main__':
    con = ConnMysql()
    con.do_select(r'SELECT user_id from tbl_vw_user WHERE telephone = 13007585173','jishulink-view-test')