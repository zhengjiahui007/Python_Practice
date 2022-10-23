
class Student():

    #类变量，实例变量
    #实例方法
    # self代表类的实例，而非类
    def __init__(self,s_name,s_age):
        #constructor function,should return None
        # initialize the paramters of class
        print("This is the Student constructor !")
        self.name_stu = s_name
        self.age_stu  = s_age

    
    name_S = 'stu'
    #age_stu = 0
    sum_stu = 0

    def do_homework(self):
        print("This is ",self.name)
        print(self.name," is ",self.age_stu," years old !")
        return

    @classmethod
    def sum_plus(cls):
        cls.sum_stu += 1
        print("The number of student is ",cls.sum_stu)
        return

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

stu1 = Student("Garry",17)
Student.sum_plus()
stu2 = Student("Ryan",17)
Student.sum_plus()
stu3 = Student("Chili",17)
Student.sum_plus()