
class GZ_Harman():
    def __init__(self,name:str,age:int,job:str) -> None:
        self.name = name
        self.age = age
        self.job = job
        return None

    def __call__(self):
        print("This GZ_Harman call !")
        return None

    def __add__(self,other):
        print("This GZ_Harman __add__ !")
        return None

    def __del__(self):
        print("Here is del GZ_Harman!")
        return None

    def __getitem__(self,item):
        print("Here is __getitem__ GZ_Harman!",item,type(item))
        return None

    def __setitem__(self,key,val):
        print("Here is __setitem__ GZ_Harman!",key,type(key),val,type(val))
        return None

    def __delitem__(self,key,val):
        print("Here is __delitem__ GZ_Harman!",key,type(key),val,type(val))
        return None

    def __iter__(self):
        self.a = 1
        return [5,4,3,2,6]
""" 
    def __next__(self):
      x = self.a
      self.a += 1
      return x
 """

list_ha = [12,3,2,6]

for i in list_ha:
    print(i)

obj_ha1 = GZ_Harman("GX",19,"Firmware")
obj_ha2 = GZ_Harman("GZ",29,"Firmware")
obj_ha2()
#obj_ha1 + obj_ha2
print(obj_ha2.__dict__) #it is a property
print(GZ_Harman.__dict__)
print(obj_ha1[3])
#del obj_ha2
obj_ha1[2]
obj_ha1[1:3:1]
obj_ha1[65] = "dkf"
print(obj_ha2.__dir__())

for i in obj_ha1:
    print(i)


