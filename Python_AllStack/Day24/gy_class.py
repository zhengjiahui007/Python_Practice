

class Person_GY():
    name_gy = "GZ"
    age_gy = 18
    sex_gy = "Female"
    def __init__(self,name,age,sex) -> None:
        print(self.name_gy,self.age_gy,self.sex_gy)
        self.name_gy = name
        self.age_gy = age
        self.sex_gy = sex
        self.gy_job = 'Engineer'
        print(self.name_gy,self.age_gy,self.sex_gy,self.gy_job)
        return None
    
    def per_print(self,Age:int,Name:str)-> None:
        print("Here is per_print , {} , {}".format(Age,Name))
        return None


p_gy = Person_GY('Garry',38,'male')
p_gy.per_print(19,'Ricky')
print("Here is  , {} , {}".format(p_gy.name_gy,p_gy.gy_job))
