"""
异常处理程序
封装器的 exception_handler 将捕获在 divide 函数中引发的任何异常，并对其进行相应处理。

try:
<语句>        #运行别的代码
except <名字>：
<语句>        #如果在try部份引发了'name'异常
except <名字>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生

"""

def Exception_Enable(flag = True):
    def Exception_Wrapper(func):
        def Exception_Handle(*arg,**kwarg):
            if (flag):
                try:
                    result = func(*arg,**kwarg)
                except Exception as e:
                    print(f"An exception occurred {str(e)} when calling {func.__name__} with arguments : {arg} , {kwarg}")
                else:
                    print(f"The calling is {func.__name__} with arguments : {arg} , {kwarg} and result is {result}")
            else:
                result = func(*arg,**kwarg)
                print(f"The calling is {func.__name__} with arguments : {arg} , {kwarg} and result is {result}")
        return Exception_Handle
    return Exception_Wrapper

@Exception_Enable(True)
def Test_Divide_Calculate(x,y):
    divi = x / y
    return divi

Test_Divide_Calculate(10,2)

Test_Divide_Calculate(10,y=0)

Test_Divide_Calculate(x = 100,y = 20)
