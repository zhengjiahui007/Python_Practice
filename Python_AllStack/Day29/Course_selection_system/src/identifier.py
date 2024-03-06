#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"
'''
说到 super， 大家可能觉得很简单呀，不就是用来调用父类方法的嘛。如果真的这么简单的话也就不会有这篇文章了，且听我细细道来。
默认用的是 Python 3，也就是说：本文所定义的类都是新式类。如果你用到是 Python 2 的话，记得继承 object:
Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx
'''
import os,sys,pickle

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
        return self.uuid

    def get_obj_by_uuid(self):
        for name in os.listdir(os.path.join(self.db_path)):
            if name == self.uuid:
                try:
                    with open(os.path.join(self.db_path, self.uuid),'rb') as file_p:
                        obj = pickle.load(file_p)
                        return obj
                except Exception as e:
                    print("An exception occurred is ",e)
                    return None
        return None

class AdminNid(NID):
    def __init__(self,db_path:str):
        super(AdminNid,self).__init__('admin',db_path)

class SchoolNid(NID):
    def __init__(self,db_path:str):
        super().__init__('school',db_path)

class TeacherNid(NID):
    def __init__(self,db_path:str):
        super().__init__('teacher',db_path)



if '__main__' == __name__:
    obj = NID('admin','dbb')
    print(type(obj))