
"""
能够在不改变原有函数的基础上，在原来的基础上添加额外的功能的代码，就叫做装饰器

装饰器模式是一种允许在运行时动态地改变对象或类功能的技术。
在Python中，装饰器实际是一种特殊的函数，装饰器函数接收一个函数作为参数，并返回一个修改后的函数，
新函数具有与原始函数相同的名称和参数。
在调用原始函数之前或之后，可执行一些额外的操作，如计时、日志记录或修改参数等



"""
import time

def log_ger(flag=True):
    def showTime(func):
        def gy_inner(*arg,**kwarg):
            start = time.time()
            func(*arg,**kwarg)
            end = time.time()
            print("Time spend is ",end - start)
            if (True == flag):
                print("Log info send !")
        return gy_inner
    return showTime
def show_log(func):
    def gz_inner(*a,**kwa):
        func(*a,**kwa)
        print("gz inner !!")
    return gz_inner

@show_log
@log_ger()
def foo(p):
    print("foo ",p)
    time.sleep(2)
    return

@log_ger(False)
def bar(y):
    print("bar ",y)
    time.sleep(3)
    return

@log_ger()
def add_func(*x):
    sum = 0
    for i in x:
        sum += i
    print("sum is ",sum)
    time.sleep(3)
    return

foo(8)
bar(6)
add_func(1,2,3,4,5,6)
