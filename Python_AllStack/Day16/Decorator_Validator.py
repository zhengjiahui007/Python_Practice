"""

 Input Validator
这个封装函数根据指定的条件或数据类型验证一个函数的输入参数。它可以用来确保输入数据的正确性和一致性。

你可结合使用位置参数和关键字参数，但必须先指定所有的位置参
数，否则解释器将不知道它们是哪个参数（即不知道参数对应的位置）。


python 使用 lambda 来创建匿名函数。

lambda只是一个表达式，函数体比def简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

语法
lambda函数的语法只包含一个语句，如下：

lambda [arg1 [,arg2,.....argn]]:expression

sum = lambda arg1, arg2: arg1 + arg2


使用 enumerate() 访问列表
在Python中使用 enumerate() 函数可以更好地实现输出列表元素及索引。

「语法格式：」

enumerate(sequence, [start=0])

「参数」

sequence -- 一个序列、迭代器或其他支持迭代的对象。

start -- 下标起始位置的值。

「返回值」

返回 enumerate(枚举) 对象。

##############################################################
函数注释(Function Annotations)
参数注释：以冒号（:）标记
返回值注释：以 -> 标记

def foo(a: expression, b: expression = 5) -> expression:
    ...


"""
""" 
seq = ["foo", "x41", "?!", "***"]

result_filter = filter(lambda x : x.isalnum(),seq)
print(result_filter)
print(list(filter(lambda x : x.isalnum(),seq)))
print(enumerate(seq))

for i,v in enumerate(seq,1):
    print(f"i = {i},v = {v}",sep = " ",end = "\n")
    print("i = {},v = {}".format(i,v),sep = " ",end = "\n")

"""
""" 
def Check_Input_Enable(flag = True):
    def Check_Input_Validator(*func_check_valid):
        def Check_Input_Func(func):
            def Check_Input_Wrapper(*arg,**kwarg):
                for i,va in enumerate(arg,start=0):

                    if ((True == isinstance(i,int)) and (i < 0)):
                        raise ValueError("Invalid argument : {}".format(i))
                for k,v in kwarg.items():
                    if (False == isinstance(v,str)):
                        raise ValueError("Invalid argument : {}".format(v))
                return func(*arg,**kwarg)
            return Check_Input_Wrapper
        return Check_Input_Func
 """
""" 
def Check_Input_Validator(flag = True,*func_check_valids):
    def Check_Input_Func(func):
        def Check_Input_Wrapper(*arg,**kwarg):
            if flag:
                for i,va in enumerate(arg,start=0):
                    print("arg : ",i,va)
                    if i < len(func_check_valids):
                        if not func_check_valids[i](va):
                            raise ValueError("Invalid argument : {}".format(i))
                for k,val in kwarg.items():
                    print("kwarg : ",k,val)
                    if k in func_check_valids[len(arg) : : 1]:
                        print("k = ",k)
                        if not func_check_valids[len(arg) : : 1][k](val):
                            raise ValueError("Invalid argument : {}".format(v))
                print(func(*arg,**kwarg))
            return 
        return Check_Input_Wrapper
    return Check_Input_Func
 """

""" 
def validate_input(flag = True,*validations):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, val in enumerate(args):
                print("args : ",i,val)
                if i < len(validations):
                    if not validations[i](val):
                        raise ValueError(f"Invalid argument: {val}")
            for key, val in kwargs.items():
                print("kwarg : ",key,val)
                if key in validations[len(args):]:
                    print("dd kwarg : ",key,val)
                    if not validations[len(args):][key](val):
                        raise ValueError(f"Invalid argument: {key}={val}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

#print(type("Iam"))

@validate_input(True,lambda x : x > 0,lambda x : x > 0,{lambda y : isinstance(y,str),lambda y : isinstance(y,str))
def Test_Input(x,y,mess_0,mess_1):
    print(mess_0,mess_1,sep = "\n",end = "\n")
    return (x + y)

Test_Input(2,8,"I am",mess_1 = " Garry")

#Test_Input(2,9,"I am"," not Garry")

 """
""" 
def decorator_add(func):
    def wrapper(a,b):
        func()
    return wrapper


@decorator_add # Test_add = decorator_add(func)
def Test_add(x,y):
    return (x + y)

Test_add()
 """



import collections
import functools
import inspect


def para_check(func):
    """
    函数参数检查装饰器,需要配合函数注解表达式(Function Annotations)使用
    """
    msg = 'Argument {argument} must be {expected!r},but got {got!r},value {value!r}'

    # 获取函数定义的参数
    # 使用inspect.signature获取函数的签名
    # 使用inspect.signature获取函数的签名后,
    # 所有参数都以key-value的形式存放在Parameter中
    sig = inspect.signature(func)
    parameters = sig.parameters  # 参数有序字典
    print("parameters is ",parameters)
    arg_keys = tuple(parameters.keys())  # 参数名称
    print("arg_keys is ",arg_keys)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        CheckItem = collections.namedtuple('CheckItem', ('anno', 'arg_name', 'value'))
        check_list = []
        print(f" CheckItem is {CheckItem.__doc__}")

        # collect args   *args 传入的参数以及对应的函数参数注解
        for i, value in enumerate(args):
            print("i is : {},value is {}".format(i,value))
            arg_name = arg_keys[i]
            print(f"arg_name is {arg_name}")
            anno = parameters[arg_name].annotation
            print(f"anno is {anno}")
            check_list.append(CheckItem(anno, arg_name, value))
            print("arg check_list is ",check_list)

        # collect kwargs  **kwargs 传入的参数以及对应的函数参数注解
        for arg_name, value in kwargs.items():
            print("arg_name is : {},value is {}".format(arg_name,value))
            anno = parameters[arg_name].annotation
            print(f"kw anno is {anno}")
            check_list.append(CheckItem(anno, arg_name, value))
            print("kwarg check_list is ",check_list)

        # check type
        for item in check_list:
            if not isinstance(item.value, item.anno):
                error = msg.format(expected=item.anno, argument=item.arg_name,
                                   got=type(item.value), value=item.value)
                raise TypeError(error)

        return func(*args, **kwargs)

    return wrapper


@para_check
def test(x : int, y : int,k : int,z : int = 3) -> int:
    return (x + y + k + z)

result_t = test(1,2,9,8)
print("result_t is ",result_t)

print(f"This is {'jello'!r}")
print("This is {!r}".format("KO"))
print(f"This is {'jello'}")

# %r是原生字符串占位符

print('This is %r'%'hello')