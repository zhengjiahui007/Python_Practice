
class Harman_Fa():
    __nameHF = "Harman"
    def __init__(self,name:str) -> None:
        self.nameHF = name
        return None
    
    def __disHarman(self,val:str):
        print("Here is __disHarman is ",val)
        return None
    
    def disHarman(self,val:str):
        print("Here is disHarman is ",val)
        return None

class Harman_So(Harman_Fa):
    __nameHS = "Harman"
    def __init__(self,name:str) -> None:
        self.nameHS = name
        super(Harman_So,self).__init__(name)
        return None
    
    def __disHarmanS(self,val:str):
        print("Here is __disHarmanS is ",val)
        return None
    
    def disHarmanS(self,val:str):
        print("Here is disHarmanS is ",val)
        self.__disHarmanS("I am GZ!")
        return None

obj_ha = Harman_So("Garry")
obj_ha.disHarmanS("I am Garry!")
#obj_ha.__disHarmanS("I am Garry!")

