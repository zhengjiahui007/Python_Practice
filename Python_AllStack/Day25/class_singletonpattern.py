
class GY_Harman():
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance:
            return cls.__instance
        else:
            cls.__instance = GY_Harman()
            return cls.__instance


obj1 = GY_Harman.get_instance()
print(obj1)

obj2 = GY_Harman.get_instance()
print(obj2)

obj3 = GY_Harman.get_instance()
print(obj3)

