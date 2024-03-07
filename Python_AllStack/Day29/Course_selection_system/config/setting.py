#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"

import os
#print(os.path.abspath(__file__),os.path.dirname(__file__),__file__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMIN_DB = os.path.join(BASE_DIR,'db','admin')
COURSE_DB = os.path.join(BASE_DIR,'db','course')
COURSE_TO_TEACHER_DB = os.path.join(BASE_DIR,'db','course_to_teacher')
CLASSES_DB = os.path.join(BASE_DIR,'db','classes')
STUDENT_DB = os.path.join(BASE_DIR,'db','student')
TEACHER_DB = os.path.join(BASE_DIR,'db','teacher')
SCHOOL_DB = os.path.join(BASE_DIR,'db','school')

if '__main__' == __name__:
    #obj = NID('admin','dbb')
    print(ADMIN_DB)
    print(os.path.join(ADMIN_DB))
    print(os.listdir(os.path.join(ADMIN_DB)))
    #os.listdir(os.path.join(self.db_path)):