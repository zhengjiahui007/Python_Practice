"""
反射简而言之就是可以通过字符串的形式来操作对象的属性和方法。

反射又叫映射、自省，它包括四个主要的函数：

setattr()、delattr()、hasattr()、getattr()

关于反射的用途，假设别人给你一个实例化的对象person，然后你需要判断这个实例是否有一个具体的属性"sex"，
用if person.sex语句去判断的话直接会报错，程序也就停止运行了，这时可以用python反射相关函数。
"""



import cls_reflection
""" 
print(getattr(cls_reflection,"gy_name"))
cls_func = getattr(cls_reflection,"gy_func")
print(cls_func("I am"))

cls_class = getattr(cls_reflection,"GY_Harman")
print(cls_class)
obj_hm = cls_class("GY",23)
print(obj_hm.gy_display("Hello"))

 """
try:
    inp_index = input("Please input a page index , for example : page_1")

    if hasattr(cls_reflection,inp_index):
        func = getattr(cls_reflection,inp_index)
        print(func())
    else:
        print("A wrong page index,404!")
except Exception as e:
    print("A exception occurred is ",e)
else:
    print("No exception occurred ! ")
finally:
    print("Page show all ! ")