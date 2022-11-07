""" 
class FooBar:
    def __init__(self,value = 42):
        self.somevar = value
        print('It is FooBar constructor function  {}!'.format(self.somevar))

gy_f = FooBar('GY')


 """
""" 
class Bird:
    def __init__(self):
        self.hungry = True

    def bird_eat(self):
        if self.hungry:
            print('Aaaah......')
            self.hungry = False
        else:
            print('No,thanks!')

class SongBird(Bird):
    def __init__(self):
        #Bird.__init__(self)
        print(super())
        super().__init__()
        self.sound = 'Squawk!'

    def sing(self):
        print(self.sound)

gy_sb = SongBird()
gy_sb.sing()
gy_sb.bird_eat()
gy_sb.bird_eat()
 """

""" 
def check_index(key):
    if not isinstance(key,int):
        raise TypeError

    if (0 > key):
        raise IndexError

class ArithmeticSequence:

    def __init__(self,start = 0,step = 1):
        self.s_start = start
        self.s_step = step
        self.s_changed = {}

    def __getitem__(self,key):
        print("This get item method!")
        check_index(key)

        try : 
            print("Seq is valid !")
            return self.s_changed[key]
        except KeyError:
            print("Seq value is invalid!")
            return self.s_start + key * self.s_step

    def __setitem__(self,key,value):
        print("Here is set item method!")
        check_index(key)

        self.s_changed[key] = value


gy_se = ArithmeticSequence(1,3)
print(type(gy_se))
print(gy_se)

print(gy_se[4])
gy_se[5] = 23
print(gy_se[5])

 """

# *args --- tuple param; **args : dict param
""" 
class CounterList(list):
    def __init__(self,*args):
        super(CounterList,self).__init__(*args)
        self.counter = 0

    def __getitem__(self,index):
        self.counter += 1
        return super(CounterList,self).__getitem__(index)

gy_cl = CounterList(range(10))
print(gy_cl)
print(gy_cl.reverse())
del gy_cl[3:6:1]

print(gy_cl)
print(gy_cl.counter)
gy_cl[4] + gy_cl[2]
print(gy_cl.counter)

 """




""" 
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self,size):
        self.width,self.height = size

    def get_size(self):
        return self.width,self.height

    size = property(get_size,set_size)

gy_r= Rectangle()
gy_r.width = 10
gy_r.height = 9

print(gy_r.size)

gy_r.size = 130,24
print(gy_r.width,gy_r.height)

 """

""" 
class GY_Test:

    @staticmethod
    def s_method():
        print("This is a static method!")

    @classmethod
    def c_method(cls):
        print("This is a class methodo of",cls)

GY_Test.s_method()
GY_Test.c_method()
 """
#把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__()
""" 
class Fibs:
    def __init__(self):
        self.a = 1
        self.b = 1
    
     def __next__(self):
         self.a,self.b = self.b,self.a + self.b
         return self.a

    def __iter__(self):
        return self


gy_fibs = Fibs()

for gy_f in gy_fibs:
    if 1000 > gy_f:
        print(gy_f,end = " ")
    else:
        break

 """
""" 
class TestIterator:
    gy_value = 0
    def __next__(self):
        self.gy_value += 1
        if (70 < self.gy_value):
            raise StopIteration
        return self.gy_value

    def __iter__(self):
        return self
    
gy_ti = TestIterator()

print(list(gy_ti))
 """

""" 
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

gy_nested = [[1,2],[3,4],[5]]

for gy_num in flatten(gy_nested):
    print(gy_num)

print(list(flatten(gy_nested)))


gy_g = ((i + 2) ** 2 for i in range(2,27))
print(type(gy_g))
print(tuple(gy_g))

print(sum(i ** 2 for i in range(0,10,1)))
 """

""" 
def flatten_recursion(nested):
    try:
        try:
            nested + ''
        except TypeError:
            print("It can go on !")
        else:
            raise TypeError("It can not go on!")
        for sublist in nested:
            for element in flatten_recursion(sublist):
                yield element
    except TypeError:
        print("It has error!")
        yield nested
    else:
        print("Hello world !")

# print("#####!")
# flatten_recursion([[1,2],[3,4],[5]])
# print("eee!")

#gy_nested = [[1,2],[3,4],[5]]
gy_nested = ['foo',['bar',['baz']]]
for gy_num in flatten_recursion(gy_nested):
    print(gy_num)

 """
""" 
def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new

gy_r = repeater(43)

#print(next(gy_r))

print(gy_r.send(None))

 """

"""
Use a tuple to store the position of each Queen, the index of tuple means the row, and the value means the column
the Queens can not in the same row or same column or same diagonal line
"""

def gy_conflict(state,next_x):
    next_y = len(state)
    for i in range(0,next_y,1):
        if (abs(state[i] - next_x) in (0,next_y - i)):
            return True
    return False

def gy_Queens(num = 8,state = ()):
    for pos in range(0,num,1):
        if not gy_conflict(state,pos):
            if (len(state) == (num - 1)):
                yield (pos,)
            else:
                for result in gy_Queens(num,state + (pos,)):
                    yield (pos,) + result

for gy_solution in gy_Queens(8):
    print(gy_solution)

