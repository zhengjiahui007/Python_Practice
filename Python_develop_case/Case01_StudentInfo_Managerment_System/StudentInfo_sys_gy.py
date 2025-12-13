# !/usr/bin/env python3
# -*- coding : utf-8 -*-
# __author__ : GarryZheng
# __date__ : 2025-12-13


import os,sys


def student_save_info():
    return


def student_show_menu():
    while True:
        print('''
        ------------学生信息管理系统------------
        |                                     |
        |=============功能菜单=================|
        |    1.录入学生信息                    |
        |    2.查找学生信息                    |
        |    3.删除学生信息                    |
        |    4.修改学生信息                    |
        |    5.排序                           |
        |    6.统计学生总人数                  |
        |    7.显示所有学生信息                |
        |    0.退出系统                        |
        |=====================================|
        |    说明：通过数字或方向键选择菜单      |
        ---------------------------------------
        ''')
        input_item = input("请选择：")
    return


def student_sys_main():
    while True:
        print("=== 学生信息管理系统登录 ===")
        stu_user = input("请输入用户名：")
        stu_pwd = input("请输入密码：")
        if(student_sys_login(stu_user,stu_pwd)):
            student_show_menu()
        else:
            print("用户名或密码错误，请重新输入！")
    return

def student_sys_login(user:str,pwd:str)->bool:
    if(('admin' == user) and ('12345' == pwd)):
        return True
    return False


if "__main__" == __name__:
    student_sys_main()

