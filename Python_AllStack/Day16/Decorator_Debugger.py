"""
Debugger
可以创建一个额外的有用的包装函数，通过打印每个函数的输入和输出来促进调试。
这种方法使我们能够深入了解各种函数的执行流程，而不必用多个打印语句来干扰我们的应用程序。
"""

import time

def Debugger_Enable(flag_enable = True):
    def Debugger_Wrapper(func):
        def Debugger_Execute(*arg,**kwarg):
            result = func(*arg,**kwarg)
            if(flag_enable):
                print("The calling function is {} with the arguments : {},{} ,the result is {}.".format(func.__name__,arg,kwarg,result))
            return result
        return Debugger_Execute
    return Debugger_Wrapper


@Debugger_Enable()
def Test_Multiply_Calculate(*a,**b):
    product = 1
    for i in a:
        product *= i
    time.sleep(3)
    return product

# f0 = Debugger_Enable(True)
# Test_Add_Calculate = (Debugger_Enable(True)(Test_Add_Calculate))(a,b)
# Test_Add_Calculate(a,b)
# (Debugger_Enable(True)(Test_Add_Calculate))(1,2,3,4,z = 5)
@Debugger_Enable(True)
def Test_Add_Calculate(*a,**b):
    sum = 0
    for i in a:
        sum += i
    time.sleep(2)
    return sum

#Test_Multiply_Calculate(3,4,5,6,y = 3)
Test_Add_Calculate(1,2,3,4,z = 5)

