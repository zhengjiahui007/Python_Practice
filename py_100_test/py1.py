#Practice 11 使用1行代码合并字典
""" first_dict = {1:'A',2:'B',"name":"Garry","location":"Shenzhen"}
second_dict = {2:'B',"Job":"Software Engineer",3:'C',"Habit":"Badminton"}

dict_result = first_dict | second_dict

print(dict_result) """

#Practice 12 查找元组中元素的索引

""" tuple_gy = ("Garry","Chili","Vincent","Joe Tian",3,"Ryan","Allen",0,32)

print(type(tuple_gy))

print("The index of Vincent is ",tuple_gy.index("Vincent")," !")

print(type({}),type([]))
print(type(set()),type(())) """

#Practice 13 将字符串转换为字符串列表
#假设你在函数中获得输出，原本应该是一个列表，但实际上却是一个字符串。

""" GY_input = "[1,2,3]"

#你可能第一时间会想到使用索引或者正则表达式。
import ast
from ipaddress import get_mixed_type_key

def string_to_list(str_para):
    return ast.literal_eval(str_para)

gy_str0 = "[2,5,8]"
gy_list0 = string_to_list(gy_str0)
print(gy_list0)

gy_str1 = "[[2,3,67],[9,2,\"difj\"],[\"tyfd\",9]]"
print(string_to_list(gy_str1))
print(type(string_to_list(gy_str1)))
print("I am an \"engineer\" ! ")
print(gy_str1)
print(type(gy_str1)) """
#实际上，使用ast模块的literal_eval方法就能搞定。

#Practice 14 计算两数差值


#计算出2个数字之间的差值。

def gy_subtract(a, b):
    return (a - b)


print((gy_subtract(1, 3)))  # -2
print((gy_subtract(3, 1)))  # 2


#上面的这个方法，需要考虑数值的先后顺序。

#使用命名参数，安排顺序，这样就不会出错了
print(gy_subtract(a = 1,b = 3))
print(gy_subtract(b = 3,a = 1))