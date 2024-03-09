#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"
#!/usr/bin/env python
import os,sys,pickle

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

from src.models import School,Course,Teacher,CourseToTeacher,Classes

def creat_school() -> None:
    print('======Creat School======')
    school_name = input("Please input the school name : ")
    obj_sch = School(school_name)
    obj_sch.save_data()
    print("School {} creat successfully !".format(obj_sch.schoolname))
    return

def show_school():
    print('======School======')
    print(School.get_all_schoonamellist())
    return


def creat_teacher():
    teacher_name = input("Please input the teacher's name : ")
    teacher_level = int(input("Please input the teacher's level : "))
    obj_teac = Teacher(teacher_name,teacher_level)
    obj_teac.save_data()
    print("Teacher %s creat successfully !" %(obj_teac.teachername))
    return

def creat_course():
    print('======Creat Course======')
    show_school()
    school_name = input("Please choose the school first : ")
    course_name = input("Please input the course name : ")
    course_price = input("Please input the course price : ")
    course_period = input("Please input the course period : ")
    school_id = School.get_uuid_by_schoolname(school_name)

    obj_course = Course(course_name, course_price, course_period,school_id)
    obj_course.save_data()
    print('Course [%s] creat successfully !' % obj_course.coursename)

def show_course():
    print('=====Show Course=====')
    course_list = Course.get_all_list()
    print(course_list)
    for item in course_list:
        print(item)
    return

def creat_course_to_teacher():
    pass

def creat_class():
    pass

def logout():
    exit()
    return

def gy_show_choice():
    choice_message = '''
        1. Creat School
        2. Show School
        3. Creat Teacher
        4. Creat Course
        5. Show Course
        6. Creat Course to Teacher
        7. Creat Class
        8. Exit
    '''
    print(choice_message)
    return

def admin_main():
    choice_dict = {
        "0" : gy_show_choice,
        "1" : creat_school,
        "2" : show_school,
        "3" : creat_teacher,
        "4" : creat_course,
        "5" : show_course,
        "6" : creat_course_to_teacher,
        "7" : creat_class,
        "8" : logout
    }
    gy_show_choice()
    while True:
        choice_input = input("Please input your choice : ")
        if choice_input not in choice_dict:
            print("Please input a choice in the list above 0 - 7!")
            continue
        choice_dict[choice_input]()
    return