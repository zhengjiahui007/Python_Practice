""" 
def gy_add(x,y):
    return (x + y)

lambda x,y : x + y

gy_lamfunc = lambda x,y : x ** y

print(gy_lamfunc(3,4))

 """

# 三元表达式
""" 
x = 1
y = 3
r = x if x > y else y
print(r)

gy_r = lambda x,y : x if x > y else y
print(gy_r(67,9))

 """
""" 
gy_list_x = [1,2,3,4,5,6,7,8,9]
gy_list_y = [2,2,3,4,5,6,7,8,10]
gy_list_z = [3,2,3,4,15,6,6,8,19]

def gy_square(x):
    return x ** 2

gy_r = map(lambda x,y,z : x * y * z,gy_list_x,gy_list_y,gy_list_z)

print(list(gy_r))

 """

""" 
gy_list_x = [1,2,3,4,5,6,7,8,9]
gy_list_y = [2,2,3,4,5,6,7,8,10]
gy_list_z = [3,2,3,6,8,19]

def gy_square(x):
    return x ** 2

gy_r = map(lambda x,y,z : x * y * z,gy_list_x,gy_list_y,gy_list_z)

print(list(gy_r))
 """

#map / reduce 映射 归约 并行计算
""" 
from functools import reduce

gy_list_x = [1,2,3,4,5,6,7,8,9]

gy_r = reduce(lambda x , y : x + y,gy_list_x,123)

print(gy_r)

 """

"""
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，
然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
"""

""" 
gy_list_x = [1,0,3,4,5,0,7,8,0]
gy_r = filter(lambda x : 0 != x,gy_list_x)

print(list(gy_r))

gy_list_c = ['q','d','S','E','w']
#gy_l = filter(lambda ch : ('a' <= ch) and ('z' >= ch),gy_list_c)
gy_l = filter(lambda ch : not ch.isupper(),gy_list_c)
print(list(gy_l))
 """















