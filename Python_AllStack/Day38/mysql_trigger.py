# -*- coding : utf-8 -*-
# __author__ : "GarryZheng"
# !/usr/bin/env python3


import os,sys,time,pymysql

gy_mysql_db = pymysql.connect(host = '127.0.0.1',port = 3306,user = 'root' , passwd = '1234' , db = 'gy_test' ,charset = 'utf8')

gy_db_cursor = gy_mysql_db.cursor()
# gy_db_cursor_dict = gy_mysql_db.cursor()

#gy_db_sql = 'insert into major_id (nid,major_name) values (%s,%s)'
gy_db_sql = 'insert into gy_tb0 (id,name) values (%s,%s)'




try:
    exe_result = gy_db_cursor.execute(gy_db_sql,('27','LQL'))
    gy_mysql_db.commit()
    print("exe result = ",exe_result)
    print(gy_db_cursor.fetchall())
except Exception as e:
    print("An error is : ",e)
    gy_mysql_db.rollback()

gy_db_cursor.close()
gy_mysql_db.close()

# BEGIN
#     IF NEW.name = 'LQL' THEN
#         INSERT INTO major_id (nid,major_name) VALUES ('8','History');
#     END IF;
# END





# 1604 corresponds to your mysql server version for the right syntax to user near $$
# CREATE TRIGGER tri_before_insert_gytb0 BEFORE INSERT gy_tb0 FOR EACH ROW



