
import time
import os
""" 
os.remove('log_file.log')

def log_cat(str_gy):
    time_format_gy = "%Y-%m-%d %X"
    gy_time_stamp = time.strftime(time_format_gy)

    with open('log_file.log','a') as gy_f:
        gy_f.write('%s , %s\n'%(gy_time_stamp,str_gy))


def log_actoin(gy_str):
    print('Start action...')
    log_cat(gy_str)


log_actoin('end action')

 """

""" 
def print_info(name,age,sex = 'boy'):
    print('My name is %s'%name)
    print('I am age %d.'%age)
    print('I am a %s.'%sex)


print_info(age = 23,name = 'Garry')
print_info(age = 33,name = 'Ellen',sex = 'girl')


 """


# 不定长参数
# *args as tuple

""" 
def gy_add(*args):
    print(args)
    sum_gy = 0
    for i in args:
        sum_gy += i
    print('The sum is %d.'%sum_gy)


gy_add(1,2,3,4,5)

def gy_print(*args,**kwargs):
    print(args)
    print(kwargs)

    for i in args:
        print(i,end = " ")
    print()

    for y,x in kwargs.items():
        print(y,x)
    
    for y in kwargs:
        print()

gy_print(2,4,1,'23','Garry',age = 23,city = 'Shz',height = 180)

 """

""" 
def gy_test():
    return 1,3,'Garry',0

print(gy_test())

a,b,c,d = gy_test()
print(a,b,c,d)

 """

""" 
if True:
    gy_x = 9

print(gy_x)

def gy_fu():
    gy_a = 8

print(gy_a)

 """
""" 
gy_x = int(2.9) #int built in

gy_count = 1 # global

def gy_outer():
    gy_out = 8 # enclosing
    gy_inner = 7
    def gy_inner():
        gy_inner = 23 # local
        print(gy_inner)

    gy_inner()


gy_outer()
 """

""" 
gy_ccount = 9

def ggy_outer():
    global gy_ccount
    print(gy_ccount)
    gy_ccount = 7
    print(gy_ccount)

ggy_outer()

 """


""" 
def ggy_outer():
    gy_ccount = 4
    print(gy_ccount)
    def gyg_inner():
        nonlocal gy_ccount # use for enclosing
        gy_ccount = 7
        print(gy_ccount)
    gyg_inner()
    print(gy_ccount)

ggy_outer()

 """

gy_ccount = 9

def ggy_outer():
    global gy_ccount
    print(gy_ccount)
    gy_ccount = 8
    print(gy_ccount)

ggy_outer()









