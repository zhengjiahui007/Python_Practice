class Human():
    sum = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.do_homework()
    
    def get_name(self):
        print("The name is %s \n"%self.name)
        return None
    
    def do_homework(self):
        print("This is Human\n")
        # print(self.name," is ",self.age_stu," years old !")
        return None

    def __do_home(self):
        print("Here is Human do home\n")
    
