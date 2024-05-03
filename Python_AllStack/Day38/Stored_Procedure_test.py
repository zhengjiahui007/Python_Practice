# -*- coding : utf-8 -*-
# __author__ : "GarryZheng"
# !/usr/bin/env python3


import os,sys,time,pymysql


gy_mysql_db = pymysql.connect(host = '127.0.0.1',port = 3306,user = 'root' , passwd = '1234' , db = 'gy_test' ,charset = 'utf8')

gy_db_cursor = gy_mysql_db.cursor()
gy_db_cursor_dict = gy_mysql_db.cursor()

gy_db_sql = 'insert into gy_tb5 (name,age,gender,major_id) values ("郑GH",19,"male",3)'



try:
    exe_result = gy_db_cursor.callproc('gy_tb5_store_procedure_t0',args = (21,))
    gy_mysql_db.commit()
    print("exe result = ",exe_result)
    print(gy_db_cursor.fetchall())
except Exception as e:
    print("An error is : ",e)
    gy_mysql_db.rollback()

gy_db_cursor.close()
gy_mysql_db.close()


# BEGIN
# 	insert into gy_tb5 (name,age,gender,major_id) values ("郑GHS",gy_store_age,"male",2);
# END