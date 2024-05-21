# _*_ coding : utf-8 _*_
# __author__ : "Garry Zheng"
#!usr/bin/env python3


import os,sys,time,math

gy_str = "abcd"
print(gy_str.upper())
print(gy_str.find('cd',0,len(gy_str)))

gy_str = "a,b,c,d"
print(gy_str.split(','),gy_str.split(',',-1))
#如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数
print("{name}喜欢{fruit}".format(name="李雷",fruit="雪梨"))
#在括号中的数字用于指向传入对象在 format() 中的位置
print("{1}喜欢{0}".format("李雷","雪梨"))

gy_str = "Python is good!"
print(gy_str.replace("Python", "python",1))

gy_str = "python修炼第一期.html"
print("1 : ",gy_str[0:11:1])
print("2 : ",gy_str.split(".")[0])
print("3 : ",gy_str[0:-5:1])
print("4 : ",gy_str[0:gy_str.find(".",0,len(gy_str)):1])

gy_str = "this is a book"
print(gy_str.replace("book", "apple",1)," , ",gy_str)
print(gy_str.startswith("this",0,len(gy_str))," , ",gy_str)
print(gy_str.endswith("apple",0,len(gy_str))," , ",gy_str)

gy_str = "This IS a book"
print(gy_str.lower()," , ",gy_str.upper())

gy_str = "this is a book\n"
print(gy_str, " , ",gy_str.rstrip("\n"))




