# -*- coding : utf-8 -*-
# __author__ : "GarryZheng"
# !/usr/bin/env python3

import os,sys,time,pymysql


gy_mysql_db = pymysql.connect(host = '127.0.0.1',port = 3306,user = 'root' , passwd = '1234' , db = 'gy_test' ,charset = 'utf8')

gy_db_cursor = gy_mysql_db.cursor()

gy_db_sql = 'insert into gy_tb5 (name,age,gender,major_id) values ("GH",19,"male",3)'

try:
    gy_db_cursor.execute(gy_db_sql)
    gy_mysql_db.commit()
except:
    gy_mysql_db.rollback()

