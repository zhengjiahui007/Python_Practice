"""
4.1 输出1-100除3余1 的数，结果为tuple
输出1-100除3余1 的数，结果为tuple
"""
""" 
gy_list = []

for gy_i in range(1,101,1):
    if (1 == gy_i%3):
        gy_list.append(gy_i)

gy_tuple = tuple(gy_list)
print(gy_tuple)
 """

"""
4.2 把2个元祖转字典
将('a', 'b', 'c', 'd', 'e') 和 (1,2, 3, 4, 5)两个tuple转成
（1， 2， 3， 4， 5）为key, ('a', 'b', 'c', 'd', 'e') 为value的字典
"""
""" 
gy_tuple_0 = ('a','b','c','d','e')
gy_tuple_1 = (1,2,3,4,5)

gy_dict = {gy_tuple_1[i] : gy_tuple_0[i] for i in range(0,len(gy_tuple_0),1)}

print(gy_dict)
 """


"""
4.3 把字典的value值转成str
将字典里的值是数值型的转换为字符串，如a = {'aa': 11, 'bb': 222}
得到{'aa': '11', 'bb': '222'}
"""
""" 
gy_dict_a =  {'aa': 11, 'bb': 222,'cc' : 343,'dd' : 987,'ee' : 985}

for gy_a_key in gy_dict_a:
    print(gy_a_key,end = " ")

print("\n")

for gy_a_value in gy_dict_a.values():
    print(gy_a_value,end = " ")

print("\n")

for gy_a_item in gy_dict_a.items():
    print(gy_a_item[0],gy_a_item[1],end = " ")

print("\n")

for gy_a_key,gy_a_value in gy_dict_a.items():
    gy_dict_a[gy_a_key] = str(gy_a_value)


print(gy_dict_a)

a = {'aa': 11, 'bb': 222}
for i in a.keys():
    a[i]=str(a[i])
print(a)

 """

"""
4.4 (1)和(1,)区别，[1]和[1,]
a = [1,2,3] 和 b = [(1),(2),(3) ] 以及 c = [(1,),(2,),(3,) ] 的区别？

"""
""" 
print(type((1)),type((1,)))
print(type([1]),type([1,]))
gy_a = [1,2,3]
gy_b = [(1),(2),(3)]
gy_c = [(1,),(2,),(3,)]

print(gy_a == gy_b,gy_a == gy_c)
print(type(gy_a),type(gy_b),type(gy_c))

 """

"""
4.5 map函数将[1，2，3，4]处理成[1,0,1,0]
map函数,有个列表a = [1, 2, 3, 4] 计算列表中每个数除以2 取出余数 得到 [1,0,1,0]
"""

""" 
def gy_map(a_list):
    for i in range(0,len(a_list),1):
        a_list[i] = a_list[i]%2
    return a_list

gy_list = [1,2,3,4]
print(gy_map(gy_list))

a = [1, 2, 3, 4]
def xx(n):
    return n%2
rs=map(xx,a)
print(list(rs))

 """

"""
.6 map函数将列表[1,2,3,4,5]转变成[1,4,9,16,25]
map函数将列表 [1,2,3,4,5] 使用python方法转变成 [1,4,9,16,25]


map() 会根据提供的函数对指定序列做映射。

第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

语法
map() 函数语法：

map(function, iterable, ...)
参数
function -- 函数
iterable -- 一个或多个序列

"""
""" 
gy_list = [1,2,3,4,5]
def square_gy(gy_n):
    return gy_n ** 2

print(list(map(square_gy,gy_list)))
 """

"""
4.7 map函数a=[1,3,5],b=[2,4,6]相乘得到[2,12,30]
map函数对列表a=[1,3,5],b=[2,4,6]相乘得到[2,12,30]
"""
""" 
gy_a = [1,3,5]
gy_b = [2,4,6]

def multi_list(gy_list_a,gy_list_b):
    return (gy_list_a * gy_list_b)

print(list(map(multi_list,gy_a,gy_b)))

 """

"""
4.8 reduce函数计算1-100的和
reduce函数计算1-100的和

reduce() 函数会对参数序列中元素进行累积。

函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，
最后得到一个结果。

参数
function -- 函数，有两个参数
iterable -- 可迭代对象
initializer -- 可选，初始参数
"""
""" 
from functools import reduce

gy_list = [x for x in range(1,101,1)]
def gy_add(gy_x,gy_y):
    return (gy_x + gy_y)

gy_sum = reduce(gy_add,gy_list)
print(gy_sum)
 """

"""
4.9 reduce函数计算10！
reduce函数计算1！+2！+3！+。。。+10！
"""
""" 
from functools import reduce

gy_factorial_list = []

for gy_i in range(1,11,1):
    factorial_i = 1
    for gy_j in range(1,gy_i + 1,1):
        factorial_i *= gy_j
    gy_factorial_list.append(factorial_i)


def gy_add(gy_x,gy_y):
    return (gy_x + gy_y)

print(reduce(gy_add,gy_factorial_list))

gy_list_n = [n for n in range(1,11,1)]

def gy_multi(x,y):
    return (x * y)

gy_factorial_list = []

for gy_i in gy_list_n:
    factorial_i = reduce(gy_multi,[m for m in range(1,gy_i + 1,1)])
    print(factorial_i)
    gy_factorial_list.append(factorial_i)

def gy_add(gy_x,gy_y):
    return (gy_x + gy_y)

print(reduce(gy_add,gy_factorial_list))

 """
"""
.10 两个字典合并a={"A":1,"B":2},b={"C":3,"D":4}
两个字典合并a={"A":1,"B":2},b={"C":3,"D":4}
"""
""" 
gy_dict_a = {"A":1,"B":2}
gy_dict_b = {"C":3,"D":4}

gy_dict_a.update(gy_dict_b)
print(gy_dict_a)

for i_key in gy_dict_b.keys():
    if i_key not in gy_dict_a.keys():
        gy_dict_a[i_key] = gy_dict_b[i_key]
print(gy_dict_a)

 """

"""
4.11 {'a':1,'b':2,'c':1} 得到 {1:['a','c'],2:['b']}
m1={'a':1,'b':2,'c':1} # 将同样的value的key集合在list里，输出{1:['a','c'],2:['b']}
"""
""" 
gy_dict_a = {'a':1,'b':2,'c':1}

gy_dict_b = {}

for gy_dict_a_vlaue in gy_dict_a.values():
    gy_list = []
    for gy_dict_key,gy_dict_value in gy_dict_a.items():
        if (gy_dict_a_vlaue == gy_dict_value):
            gy_list.append(gy_dict_key)
    #gy_dict_b[gy_dict_a_vlaue] = gy_list
    gy_dict_b.setdefault(gy_dict_a_vlaue,gy_list)

print(gy_dict_b)
 """

"""
4.12 字典按key排序d={"name":"zs","age":18,"}
d={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
字典根据键从小到大排序
"""
""" 
gy_d = {"name":"zs","age":18,"city":"深圳","tel":"1362626627"}

gy_keys = sorted(gy_d.keys(),reverse = False)
gy_dict_c = {}
for i in gy_keys:
    gy_dict_c[i] = gy_d[i]

print(gy_d)
print(gy_dict_c)

 """

"""
4.13 集合（交集、差集、并集）
a = [2, 3, 8, 4, 9, 5, 6]
b = [2, 5, 6, 10, 17, 11]
1.找出a和b中都包含了的元素
2.a或b中包含的所有元素
3.a中包含而集合b中不包含的元素
"""

gy_a = {2, 3, 8, 4, 9, 5, 6}
gy_b = {2, 5, 6, 10, 17, 11}

print(gy_a.intersection(gy_b))
print(gy_a.union(gy_b))
print(gy_a.difference(gy_b))









