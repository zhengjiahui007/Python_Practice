#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"

'''
pickle模块中常用的函数：
pickle.dump(obj, file, [,protocol])
含义：pickle.dump（对象，文件，[使用协议]）
将要持久化的数据“对象”，保存到“文件”中，使用有3种协议，索引0为ASCII，1为旧式二进制，2为新式二进制协议，不同之处在于2要更高效一些。
默认dump方法使用0做协议
pickle.load(file)
含义：pickle.load(文件)，将file中的对象序列化读出。
从“文件”中读取字符串，将他们反序列化转换为python的数据对象，可以像操作数据类型的这些方法来操作它们；　　
pickle.dumps(obj[, protocol])
函数的功能：将obj对象序列化为string形式，而不是存入文件中。
obj：想要序列化的obj对象。
protocal：如果该项省略，则默认为0。如果为负值或HIGHEST_PROTOCOL，则使用最高的协议版本。
pickle.loads(string)
函数的功能：从string中读出序列化前的obj对象。
string：文件名称。
'''

import os,sys,time,pickle

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

from config import setting
from src import identifier

class BaseModel:
    def __init__(self,nid:str,dbpath:str):
        self.nid = nid
        self.db_path = dbpath

    def save_data(self):
        db_file_name = str(self.nid)
        db_file_path = os.path.join(self.db_path,db_file_name)
        with open(db_file_path,'wb') as file_p:
            pickle.dump(self,file_p)

class Admin(BaseModel):
    db_path = setting.ADMIN_DB

    def __init__(self,username:str,password:str):
        self.nid = identifier.AdminNid(Admin.db_path)
        self.username = username
        self.password = password
        self.creat_time = time.strftime('%Y-%m-%d')
        super(Admin,self).__init__(self.nid,Admin.db_path)

    @staticmethod
    def login_admin(user:str,pwd:str):
        '''
        但在try except finally中顺序有点特殊
        1.不管怎样，finally代码总会执行
        2.try except finally语句的return是暂存起来，执行到return时，并没有直接返回`
        '''
        obj_ret = None
        try:
            for item_name in os.listdir(os.path.join(Admin.db_path)):
                print(item_name)
                if item_name != "__init__.py":
                    with open(os.path.join(Admin.db_path,item_name),'rb') as file_p:
                        obj = pickle.load(file_p)
                        if (user == obj.username) and (pwd == obj.password):
                            obj_ret = obj
                            break
        except Exception as e:
            print('An exception occurred is ',e)
        finally:
            return obj_ret

class School(BaseModel):
    db_path = setting.SCHOOL_DB
    def __init__(self,sc_name:str):
        self.schoolname = sc_name
        self.nid = identifier.SchoolNid(School.db_path)
        self.income = 0

    def __str__(self) -> str:
        return self.schoolname

    @staticmethod
    def get_all_schoollist() -> list:
        schoolname_list = []
        try:
            for school_file in os.listdir(os.path.join(School.db_path)):
                """
                使用 with 关键字系统会自动调用 f.close() 方法， with 的作用等效于 try/finally 语句是一样的。
                with 语句实现原理建立在上下文管理器之上。
                上下文管理器是一个实现 __enter__ 和 __exit__ 方法的类。
                使用 with 语句确保在嵌套块的末尾调用 __exit__ 方法。
                """
                if school_file != "__init__.py":
                    with open(os.path.join(School.db_path,school_file),'rb') as file_p:
                        school_obj = pickle.load(file_p)
                        schoolname_list.append(school_obj.schoolname)
        except Exception as e:
            print('An exception occurred is ',e)
            return None
        return schoolname_list

if '__main__' == __name__:
    obj_ad = Admin('Garry','1234')
    obj_ad.save_data()
    obj_ad = Admin('XXG','1234')
    obj_ad.save_data()
    obj_ad = Admin('ROOT','1234')
    obj_ad.save_data()
    print(Admin.login_admin('XX1G','1234'))
    # obj_sc = School("SCUT")
    # obj_sc.save_data()
    # obj_sc = School("ZHONGSHAN")
    # obj_sc.save_data()
    # obj_sc = School("BEIJING")
    # obj_sc.save_data()
    # print(School.get_all_schoollist())


