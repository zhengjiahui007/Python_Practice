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
