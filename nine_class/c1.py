
#from night_class.c2 import Human

from c2 import Human

class Student(Human):

    #类变量，实例变量
    #实例方法
    # self代表类的实例，而非类
    def __init__(self,s_school,s_name,s_age):
    #constructor function,should return None
    # initialize the paramters of class
        print("This is the Student constructor !")
        self.school = s_school
        #Human.__init__(self,s_name,s_age)
        super(Student,self).__init__(s_name,s_age)

    name_S = 'stu'
    age_stu = 0
    sum_stu = 0

    def do_homework(self):
        print("This is ",self.name)
        #super(Student,self).do_homework()
        print(self.name," is ",self.age_stu," years old !")
        return

    @classmethod
    def sum_plus(cls):
        cls.sum_stu += 1
        print("The number of student is ",cls.sum_stu)
        return

    def __do_home(self):
        print("Here is Studend do home\n")

""" 
stu1 = Student()
stu2 = Student()
stu3 = Student()

print(id(stu1))
print(id(stu2))
print(id(stu3)) """

""" stud1 = Student("GarryZheng",37)

print(stud1.name_stu,stud1.age_stu)
print(Student.name_S,Student.sum_stu) """

#stu1 = Student("SCUT","Garry",17)
# print(stu1.name,stu1.age)
# Student.sum_plus()
# stu1.get_name()
# stu1.do_homework()

#stu2 = Student("Ryan",17)
#Student.sum_plus()
#stu3 = Student("Chili",17)
#Student.sum_plus()
"""  
class A(object):

    def __init__(self):
        self.__Gender()
        self.Name()

    def __Gender(self):
        print("A.__Gender()")

    def Name(self):
        print("A.Name()")

class B(A):

    def __Gender(self):
        print("B.__Gender()")

    def Name(self):
        print("B.Name()")
b = B()
 """