""" 
class Person:

    def set_name(self,gy_name):
        self.name = gy_name

    def get_name(self):
        return self.name

    def greet(self):
        print("Hello,world! I'm {}.".format(self.name))


gy_foo = Person()
gy_bar = Person()

gy_foo.set_name("Garry Zheng")
gy_bar.set_name("Ryan Xu")

gy_foo.greet()
gy_bar.greet()

print(gy_foo.name)
gy_bar.name = "Vincent Song"
gy_bar.greet()
 """
""" 
class Secretive:
    def __inaccessible(self):
        print("Bet you can't see me ...!")

    def accessible(self):
        print("The secret message is : ")
        self.__inaccessible()


gy_s = Secretive()
gy_s._Secretive__inaccessible()
# gy_s.accessible()
 """
""" 
class Filter:
    def __init__(self):
        self.blocked = []

    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked]
    
class SPMAFilter(Filter):
    def __init__(self):
        self.blocked = ["SPAM"]

gy_f = SPMAFilter()
print(gy_f.filter(["SPAM","egg","dogs"]))

print(issubclass(SPMAFilter,Filter),issubclass(Filter,SPMAFilter))
print(SPMAFilter.__bases__,Filter.__bases__)
print(isinstance(gy_f,SPMAFilter),isinstance(gy_f,Filter))
print(gy_f.__class__)
 """
""" 
class Calculator:
    def calculate(self,expression):
        self.value = eval(expression)

    def talk(self):
        print('Hello,my value is ',self.value)

class Talker:
    def talk(self):
        print('Hi,my value is ',self.value)

# pay attention to the order of the super classes
class TalkingCalculator(Calculator,Talker):
    pass

gy_tc = TalkingCalculator()
gy_tc.calculate('1 + 2 * 4')
gy_tc.talk()

print(hasattr(gy_tc,'talk'),hasattr(gy_tc,'fnord'),callable(getattr(gy_tc,'talk',None)))
setattr(gy_tc,'name','Garry Zheng')
print(gy_tc.name)
print(gy_tc.__dict__)

 """

 # abstract class

from abc import ABC,abstractmethod

class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass

class Knigget(Talker):
    def talk(self):
        print("Hi,this is Knigget\n")

gy_k = Knigget()
print(isinstance(gy_k,Talker))
gy_k.talk()

class Herring:
    def talk(self):
        print('Hello, this is Herring\n')

gy_h = Herring()
print(isinstance(gy_h,Talker))