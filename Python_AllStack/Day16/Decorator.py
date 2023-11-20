
"""
能够在不改变原有函数的基础上，在原来的基础上添加额外的功能的代码，就叫做装饰器

装饰器模式是一种允许在运行时动态地改变对象或类功能的技术。
在Python中，装饰器实际是一种特殊的函数，装饰器函数接收一个函数作为参数，并返回一个修改后的函数，
新函数具有与原始函数相同的名称和参数。
在调用原始函数之前或之后，可执行一些额外的操作，如计时、日志记录或修改参数等


Python 封装器是添加到另一个函数中的函数，然后可以添加额外的功能或修改其行为，
而不直接改变其源代码。它们通常以装饰器的形式实现，
这是一种特殊的函数，将另一个函数作为输入，并对其功能进行一些修改。

封装器函数在各种情况下都很有用：

功能扩展（Functionality Extension）：我们可以通过用装饰器包装我们的函数来增加诸如日志、性能测量或缓存等功能。
代码可重用性：我们可以将一个封装函数甚至一个类应用于多个实体，你可以避免代码的重复，并确保不同组件的行为一致。
行为修改：我们可以拦截输入参数，例如，验证输入变量，而不需要许多assert行。

"""
import time

#def log_ger(flag=True):
def showTime(func):
    print("Enter showTime")
    def gy_inner(*arg,**kwarg):
        print("enter gy inner !!")
        start = time.time()
        func(*arg,**kwarg)
        end = time.time()
        print("Time spend is ",end - start)
        print("leave gy inner !!")
            #if (True == flag):
                #print("Log info send !")
    print("Leave showTime")
    return gy_inner
#    return showTime
def show_log(func):
    print("Enter show_log")
    def gz_inner(*a,**kwa):
        print("enter gz inner !!")
        func(*a,**kwa)
        print("leave gz inner !!")
    print("Leave show_log")
    return gz_inner

#@showTime
@show_log
def foo(p):
    print("foo ",p)
    time.sleep(2)
    return

#@log_ger(False)
def bar(y):
    print("bar ",y)
    time.sleep(3)
    return

#@log_ger()
def add_func(*x):
    sum = 0
    for i in x:
        sum += i
    print("sum is ",sum)
    time.sleep(3)
    return

# foo(8)
# bar(6)
# add_func(1,2,3,4,5,6)

def decorator_one(func):
    print('Decorator one before 0.')
    def wrapper():
        print('Decorator one before.')
        func()
        print('Decorator one after.')
    return wrapper

def decorator_two(func):
    def wrapper():
        print('Decorator two before.')
        func()
        print('Decorator two after.')
    return wrapper

@decorator_one
@decorator_two
def say_hello():
    print('Hello World!')

#say_hello()