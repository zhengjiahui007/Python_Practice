
'''
python-类的继承 构造方法的重写及继承
https://zhuanlan.zhihu.com/p/345723147
'''

class Fa_gy():
    def __init__(self, name, age):
        return None

    def fa_f0(self):
        print("fa_f0")
        return None

    def fa_f1(self):
        print("fa_f1")
        return None

class Son_gy(Fa_gy):
    def __init__(self, name, age):
        return None

    def fa_f1(self):
        super(Son_gy,self).fa_f1() #call the base class fa_f1
        Fa_gy.fa_f1(self) #call the base class fa_f1
        print("son_f1")
        return None

obj_gy = Son_gy("GY",19)
obj_gy.fa_f1()
obj_gy.fa_f0()