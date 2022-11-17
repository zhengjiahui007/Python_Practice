import time
""" 
def gy_time():
    print('This is a gy_time!')

def gy_time1():
    print('This is a gy_time1!')

def print_current_time(func_p):
    print(time.time())
    func_p()



print_current_time(gy_time)
print_current_time(gy_time1)
 """


# Decorator , 装饰器

def gy_decorator(gy_func):
    def gy_wrapper(*args,**kw):
        print(time.time()," this is decorator !")
        gy_func(*args,**kw)
    return gy_wrapper

@gy_decorator
def gy_time(f_name):
    print('This is a gy_time! ' + f_name)

@gy_decorator
def gy_time1(f_name,f_name_2):
    print('This is a gy_time! ' + f_name_2 + f_name)


@gy_decorator
def gy_time2(f_name,f_name_2,**kw):
    print('This is a gy_time! ' + f_name_2 + f_name)
    print(kw)


# gy_func = gy_decorator(gy_time)
# gy_func()

gy_time('gy test func')

gy_time1('gy test func1','hello')

gy_time2('gy test func2','hello22',gy_a = 2,gy_b = 0,gy_c = [1,2,3])










