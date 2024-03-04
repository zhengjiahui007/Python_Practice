#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"

import os,sys

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

from lib import commons

class NID:
    def __init__(self,role:str,db_path:str):
        '''
        :param role : school,teacher,student...
        :db_path : the path of the data base
        :return : None
        '''
        role_list = [
            'admin','school','teacher','course','course_to_teacher','classed','student'
        ]
        if role not in role_list:
            raise Exception("The role is not correct,please input a role in {}".format(role_list))
            #raise Exception("The role is not correct,please input a role in %s" % ','.join(role_list))
        self.role = role
        self.uuid = commons.creat_uuid()
        self.db_path = db_path
    
    def __str__(self):
        return

if '__main__' == __name__:
    obj = NID('amin','dbb')
    print(type(obj))