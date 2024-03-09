#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"
#!/usr/bin/env python

from src.models import Admin


def initialize()->bool:
    try:
        user = input("Pleas input the user name : ")
        pwd = input("Please input the password : ")
        obj_ad = Admin(user,pwd)
        obj_ad.save_data()
    except Exception as e:
        print(initialize.__name__," An exception occured e ",e)
        return False
    else:
        return True

def main()->bool:
    try:
        dis_playmessage = """
        1.Initialize an Administrative account.
        """
        choice_dict = {
            "1" : initialize
        }
        while True:
            print(dis_playmessage)
            choice = input("Please input your choice : ")
            '''
            Python 字典 in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false。
            而 not in 操作符刚好相反，如果键在字典 dict 里返回 false，否则返回 true。
            '''
            if choice not in choice_dict:
                print("Your choice is not in the preset list,please input a correct chioce")
                continue
            if choice_dict[choice]():
                print("Creat AD successfully !")
                return True
            else:
                print("Creat AD failed !")
                return False
    except Exception as e:
        print("An exception occured e ",e)
        return False


