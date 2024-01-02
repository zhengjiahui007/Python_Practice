
class Harman_gz():
    def __init__(self) -> None:
        return None
    
    def har_print(self):
        print("This is common method !")
        return None

    @staticmethod
    def har_staprint(a:int,b:str):
        print("This is static method ! a {} b {} !".format(a,b))
        return None

    @classmethod
    def har_classprint(cls,a:int,b:str):
        print("This is class method ! a {} b {} cls {}!".format(a,b,cls))
        return None


obj_gz = Harman_gz()
obj_gz.har_print()

obj_gz1 = Harman_gz()
Harman_gz.har_print(obj_gz1)
Harman_gz.har_staprint(9,"GZ")
Harman_gz.har_classprint(4,'df')