
class Province():
    Country = "China"
    def __init__(self,name_prov:str) -> None:
        self.name = name_prov

        return None
    
    def prov_display(self):
        print("The country is ",self.Country,self.name)
        return None

print(f"Province country is {Province.Country}")
print("Province country is",Province.Country)
print("Province country is {}".format(Province.Country))
print("Province country is %s" %Province.Country)

obj_prov = Province("Guangdong")
obj_prov.prov_display()
