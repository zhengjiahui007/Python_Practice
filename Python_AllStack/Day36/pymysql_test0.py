# -*- coding : utf-8 -*-
# __author__ : "GarryZheng"
# !/usr/bin/env python3

import os,sys,time,pymysql


gy_mysql_db = pymysql.connect(host = '127.0.0.1',port = 3306,user = 'root' , passwd = '1234' , db = 'gy_test' ,charset = 'utf8')

gy_db_cursor = gy_mysql_db.cursor()
gy_db_cursor_dict = gy_mysql_db.cursor(cursor = pymysql.cursors.DictCursor)

gy_db_sql = 'insert into gy_tb5 (name,age,gender,major_id) values ("郑GH",19,"male",3)'
gy_db_sql1 = 'insert into gy_tb5 (name,age,gender,major_id) values (%s,%s,%s,%s)'
gy_db_sql2 = 'update gy_tb5 set name="郑嘉惠" where id=11'
gy_db_sql3 = 'select * from gy_tb5'
# gy_input = input("Please input the name|age|gender|major id : ")
# input_param_list = gy_input.split('|')
# print(" input_param_list = ",input_param_list)
# input_age = int(input_param_list[1])
# input_majorid = int(input_param_list[3])
# print(" age majorid = ",input_age,input_majorid)

input_param_list = [('ZJSS', '16', 'female', '2'),('ZJSDL', '15', 'female', '1'),('DZJLL', '15', 'female', '2')]
input_param_lHist1 = [['HSS', '16', 'female', '2'],['HJSDL', '15', 'female', '1'],['HZJLL', '15', 'female', '2']]

try:
    #exe_result = gy_db_cursor.execute(gy_db_sql2)
    #exe_result = gy_db_cursor.execute(gy_db_sql1,input_param_list)
    #exe_result = gy_db_cursor.executemany(gy_db_sql1,input_param_lHist1)
    #exe_result = gy_db_cursor.execute(gy_db_sql3)
    exe_result = gy_db_cursor_dict.execute(gy_db_sql3)
    print("exe result = ",exe_result)
    print(gy_db_cursor_dict.fetchall())
    gy_mysql_db.commit()
except Exception as e:
    print("An error is : ",e)
    gy_mysql_db.rollback()

gy_db_cursor.close()
gy_mysql_db.close()
