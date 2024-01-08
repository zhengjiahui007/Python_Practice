""" 
gy_name = "GarryZheng"

def gy_func(msee : str):
    return "I am GZ!"


class GY_Harman():
    pass
    def __init__(self,nm:str,age:int):
        self.name = nm
        self.age = age
        return None
    
    def gy_display(self,mss:str):
        return "%s - %s - %s " %(self.name,self.age,mss)

 """
""" 
obj_gy = GY_Harman("GZ",39)
print(hasattr(obj_gy,'gy_display'))
obj_funcdis = getattr(obj_gy,"gy_display")
print(obj_funcdis("engineer"))
setattr(obj_gy,'job',"Firmware Engineer")
print(obj_gy.job)
print(hasattr(obj_gy,'job'))
delattr(obj_gy,"job")
print(hasattr(obj_gy,'job'))
 """

def page_1():
    return "Page1"

def page_2():
    return "Page2"

def page_3():
    return "Page3"

def page_4():
    return "Page4"