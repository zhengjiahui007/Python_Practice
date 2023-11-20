"""
1 — Timer
这个封装器函数测量一个函数的执行时间，并打印出已用的时间。它对于剖析和优化代码非常有用。
"""

"""
#参数前面的星号将提供的所有值都放在一个元组中，也就是将这些值收集起来
def print_params_2(title, *params):
print(title)
print(params)
并尝试调用它：
print_params_2('Params:', 1, 2, 3)
Params:
(1, 2, 3)


要收集关键字参数，可使用两个星号。
def print_params_3(**params):
print(params)
print_params_3(x=1, y=2, z=3)
{'z': 3, 'x': 1, 'y': 2}
如你所见，这样得到的是一个字典而不是元组
"""
###print("The number of {} in {} is {} !".format(gy_str_sub,gy_string,gy_count_sub))


import time

def Calculate_Time_Enable(flag = False):
    def Calculate_Timer(func):
        def Calculate_Wrapper(*arg,**kwarg):
            start_time = time.time()
            result_func = func(*arg,**kwarg)
            end_time = time.time()
            executed_time = end_time - start_time
            if(True == flag):
                print("The {} executed time is {},result is {}".format(func.__name__,executed_time,result_func))
            else:
                print("The {} result is {}".format(func.__name__,result_func))
            return result_func
        return Calculate_Wrapper
    return Calculate_Timer

@Calculate_Time_Enable(True)
def Test_Add_Calculate(*a,**b):
    sum = 0
    for i in a:
        sum += i
    time.sleep(2)
    return sum

@Calculate_Time_Enable(False)
def Test_Multiply_Calculate(*a,**b):
    product = 1
    for i in a:
        product *= i
    time.sleep(3)
    return product

Test_Add_Calculate(1,2,3,4,5)

Test_Multiply_Calculate(2,3,4,5,6)
