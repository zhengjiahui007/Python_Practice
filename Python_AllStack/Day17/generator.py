# !/usr/bin/env python3
# -*- coding : utf-8 -*-
# __author__ : "GarryZheng"
# Date : 2024-06-06

import os,sys,time

'''
生成器是一种特殊类型的迭代器
# 一种是生成器函数:gy_generator
# 另一种是生成器表达式 (gy_fun(a) for a in range(0,10,1))
https://blog.csdn.net/weixin_44244190/article/details/131848927
https://blog.csdn.net/2401_84615650/article/details/138224082

1.第一种方法:

a = (x for x in range(5))
print(a)
print(next(a))
print(a.__next__())
for i in a:
    print(i)


2.第二种方法:

def fun(n):
    for i in range(n):
        yield i
b = fun(5)
print(b)
print(next(b))
print(b.__next__())



生成器的send方法
def fun(n):
    for i in range(n):
        k = yield i
        print(k)
b = fun(5)
b.send(None)    # 或者next(b)/b.__next__()
b.send('a')
b.send('b')
1
2
3
4
5
6
7
8
输出结果：

a
b
1
2
总结
yield的用法是：记住上一次返回时在函数体中的位置，调用此函数从上一次返回的位置开始执行。
send的用法时：send()方法返有一个参数，该参数指定的是上一次被挂起的yield语句的返回值。
区别：当send()的参数为None时，正好与next方法等价。在调用send()方法时，要么先调用一次next()到函数挂起的位置，或者直接send(None)。
————————————————

                            版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。
                        
原文链接：https://blog.csdn.net/qq_1290259791/article/details/80994192
'''
# method 1
def gy_generator():
    print("112")
    yield 1
    print("13312")
    yield 4
    return None

def gy_function():
    return 1

def gy_fun(n):
    return n**4

#0,1,1,2,3,5,8,13,21,34
def gy_fibonacci(max_val:int,lst_fib:list):
    n_val,n_before,n_after = 0,0,1
    lst_fib.append(n_before)
    while (n_val <= max_val):
        lst_fib.append(n_after)
        # n_temp = n_after
        # n_after = (n_before + n_after)
        # n_before = n_temp
        n_before,n_after = n_after,n_before + n_after
        n_val += 1
    return None
        
def gy_fibonacci_gen(max_val:int):
    n_val,n_before,n_after = 0,0,1
    while (n_val <= max_val):
        yield n_before
        n_before,n_after = n_after,n_before + n_after
        n_val += 1
    return None

def garry_gen():
    print("111")
    ret = yield 1
    print("1 ret = ",ret)

    print("222")
    ret = yield 2
    print("2 ret = ",ret)

    print("333")
    ret = yield 3
    print("3 ret = ",ret)

if (__name__ == "__main__"):
    #### fibonacci 函数方式----------------------------------------###
    # gy_lst_fib = []
    # gy_fibonacci(10,gy_lst_fib)
    # print(gy_lst_fib)

    #### fibonacci 生成器方式----------------------------------------###
    fib_gen = gy_fibonacci_gen(18)
    """
    print(next(fib_gen))
    print(next(fib_gen))
    print(next(fib_gen))
    print(next(fib_gen))
    """
    """
    try:
        for i in fib_gen:
            print(i,end = " ")
    except Exception as e:
        print(e)
    """

    gz_gen = garry_gen()
    print(gz_gen.send(None))
    print(gz_gen.send("wer"))
    print(gz_gen.send("sdf"))
    # print(gz_gen.send("DWE"))
    ####----------------------------------------###
    #生成器---yield方式
    # print(gy_generator(),type(gy_generator))
    # print(gy_function(),type(gy_function))

    # gz_gen = gy_generator()
    # print(gz_gen,type(gz_gen))
    # a = next(gz_gen)
    # b = next(gz_gen)
    # print(a,b)

    ####----------------------------------------###
    #列表/集合/字典/元组生成式
    # gy_lst = [gy_fun(a) for a in range(0,10,1)]
    # print(gy_lst,type(gy_lst))

    # gy_set = {a for a in range(0,10,1)}
    # print(gy_set,type(gy_set))

    # gy_dic = {a : a*2 for a in range(0,10,1)}
    # print(gy_dic,type(gy_dic))
    
    # gy_gen = (gy_fun(a) for a in range(0,10,1))
    # print(gy_gen,type(gy_gen))
    # print(next(gy_gen))
    # print(next(gy_gen))
    # print(next(gy_gen))
    # print(next(gy_gen))
    # print(next(gy_gen))
    # print(next(gy_gen))
    # print(next(gy_gen))
    # print(next(gy_gen))
    # print(next(gy_gen))
    # print(next(gy_gen))    
    # for i in gy_gen:
    #     print(i,end = " ")

    # gy_tup = tuple(gy_gen)
    # print(gy_tup,type(gy_tup))

