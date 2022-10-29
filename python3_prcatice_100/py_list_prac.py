"""
3.1 反转（判断对称）
如何判断一个数组是对称数组：
要求：判断数组元素是否对称。例如[1，2，0，2，1]，[1，2，3，3，2，1]这样的都是对称数组
用Python代码判断，是对称数组打印True，不是打印False,如：
x = [1, "a", 0, "2", 0, "a", 1]
"""
""" 
gy_list = [1,"a",0,"2",0,"b",1]

if (gy_list[::1] == gy_list[::-1]):
    print(True)
else:
    print(False)
 """

"""
3.2列表切片
如果有一个列表a=[1,3,5,7,11]
问题：1如何让它反转成[11,7,5,3,1]
2.取到奇数位值的数字，如[1,5,11]
"""
""" 
gy_list = [1,3,5,7,11]
print(gy_list[::-1])
print(gy_list[::2]) """

"""

3.3列表大小排序
问题：对列表a 中的数字从小到大排序
a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
"""
""" 
gy_list = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]

gy_list.sort()
print(gy_list)
gy_list_1 = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
print(sorted(gy_list_1))

print(gy_list_1)
 """

"""
3.4 取出最大值最小值
L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
找出列表中最大值和最小值
"""

""" 
gy_L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]

print(len(gy_L1),max(gy_L1),min(gy_L1))

print(sorted(gy_L1))

#gy_L2 = gy_L1 # a wrong way to assign a list to another list
#gy_L2 = gy_L1.copy()
#gy_L2 = gy_L1[::1]
gy_L2 = list(gy_L1)

gy_L2.sort()

print(gy_L2)
print(gy_L1)
 """

"""
3.5 找出列表中单词最长的一个
a = ["hello", "world", "yoyo", "congratulations"]
找出列表中单词最长的一个

sort/sorted
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
"""
""" 
gy_a = ["hello", "world", "yoyo", "congratulations"]

gy_b = sorted(gy_a,key=len,reverse=True)
print(gy_a)
print(gy_b[0])

gy_a.sort(key=len,reverse=False)
print(gy_a[-1])
 """

"""
3.6 切片取出列表中最大的三个数
取出列表中最大的三个值
L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
"""
""" 
gy_L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
gy_L1.sort(reverse=True)
print(gy_L1[0:3:1])
 """

"""
3.7列表按绝对值排序
a = [1, -6, 2, -5, 9, 4, 20, -3] 按列表中的数字绝对值从小到大排序
"""
""" 
gy_a = [1, -6, 2, -5, 9, 4, 20, -3]
gy_b = sorted(gy_a,key = abs,reverse = False)
print(gy_a)
print(gy_b)
 """

"""
3.8按字符串长度排序
b = ["hello", "helloworld", "he", "hao", "good"]
按list里面单词长度倒叙
"""

""" 
gy_b = ["hello", "helloworld", "he","h3e","hao", "good"]

gy_a = sorted(gy_b,key = len,reverse = True)
print(gy_a)

##########################
b = ["hello", "helloworld", "he","h3e","hao", "good"]
lens=[]
for i in b:
    lens.append(len(i)) #将每个字符串的长度放在列表中
lens.sort(reverse=True)
print(lens) #长度列表，降序
for i in b:
    num=lens.index(len(i)) #找到索引位置
    lens[num]=i #将相应索引位置替换为字符串
    print(lens)
print(lens)

 """

"""
3.9去重与排序
L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
如何用一行代码得出[1, 2, 3, 5, 11, 33, 88]
L2 = [1, 2, 3, 4, 5] ,L[10:]结果是多少（报错？还是None，还是[]）
"""
""" 
gy_L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
gy_L2 = []

for gy_l in gy_L1:
    if gy_l not in gy_L2:
        gy_L2.append(gy_l)
print(gy_L2)

gy_L3 = [1,2,3,4,5]
print(gy_L3[10:])

gy_L4 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
print(sorted(list(set(gy_L4))))
 """

"""
3.10 去重保留顺序
将列表中的重复值取出(仅保留第一个)，要求保留原始列表顺序
如a=[3, 2, 1, 4, 2, 6, 1] 输出[3, 2, 1, 4, 6]
"""
""" 
gy_a = [3, 2, 1, 4, 2, 6, 1]
gy_b = []
for gy_i in gy_a:
    if gy_i not in gy_b:
        gy_b.append(gy_i)

print(gy_b)
 """

"""
3.11 列表合并
a = [1, 3, 5, 7]
b = ['a', 'b', 'c', 'd']
如何得到[1, 3, 5, 7, 'a', 'b', 'c', 'd']
"""
""" 
gy_a = [1, 3, 5, 7]
gy_b = ['a', 'b', 'c', 'd']
gy_c = gy_a + gy_b
print(gy_c)
 """

"""
3.12 生成列表(列表推导式)
用一行代码生成一个包含 1-10 之间所有偶数的列表
"""
""" 
gy_even = []

for gy_i in range(2,11,2):
    gy_even.append(gy_i)
print(gy_even)

#列表推导式
gy_even_1 = [x for x in range(2,11,2)]
print(gy_even_1)

 """

"""
3.13 列表成员的平方
列表a = [1,2,3,4,5], 计算列表成员的平方数，得到[1,4,9,16,25]
"""
""" 
gy_a = [1,2,3,4,5]
gy_aa = [x**2 for x in gy_a]
print(gy_aa)

 """

"""
3.14 找出列表大于0的数
使用列表推导式，将列表中a = [1, 3, -3, 4, -2, 8, -7, 6]
找出大于0的数，重新生成一个新的列表
"""
""" 
gy_a = [1, 3, -3, 4, -2, 8, -7, 6]

gy_a_more_than_0 = [x for x in gy_a if 0 < x]
print(gy_a_more_than_0)

 """

"""
3.15统计列表有多少大于0
统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
"""
""" 
gy_a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]

gy_a_positivecount = 0
gy_a_negativecount = 0

for gy_i in gy_a:
    if 0 < gy_i:
        gy_a_positivecount += 1
    elif 0 > gy_i:
        gy_a_negativecount += 1
        
print(gy_a_positivecount,gy_a_negativecount)
 """

"""
3.16列表排除筛选
a = ["张三","张四","张五","王二"] 如何删除姓张的
"""
""" 
gy_a = ["张三","张四","张五","王二"]
gy_a_0 = gy_a.copy()
print(id(gy_a),id(gy_a_0))
print(gy_a)
print(gy_a_0)
gy_n = 0
for gy_i in range(0,len(gy_a),1):
    if ("张" == gy_a[gy_i][0]):
        del gy_a_0[gy_i - gy_n]
        gy_n += 1
        
print(gy_a)
print(gy_a_0)

 """
"""
3.17列表过滤(filter)
题1：有个列表a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8] 使用filter 函数过滤出大于0的数
题2：列表b = ["张三", "张四", "张五", "王二"] 过滤掉姓张的姓名

filter :
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。

该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，
然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
"""
""" 
gy_a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]

def is_positive(integer_para):
    if (0 < integer_para):
        return True
    else:
        return False

gy_c = filter(is_positive,gy_a)
print(list(gy_c))

def family_name_Zhang(gy_name):
    if ("张" == gy_name[0]):
        return False
    else:
        return True

gy_b = ["张三", "张四", "张五", "王二"]
gy_d = filter(family_name_Zhang,gy_b)
print(list(gy_d))
 """

"""
3.18过滤列表中不及格学生(filter)
过滤掉列表中不及格的学生
a = [
{"name": "张三", "score": 66},
{"name": "李四", "score": 88},
{"name": "王五", "score": 90},
{"name": "陈六", "score": 56},
]
"""
""" 
gy_a = [
{"name": "张三", "score": 66},
{"name": "李四", "score": 88},
{"name": "王五", "score": 90},
{"name": "陈六", "score": 56},
]

def pass_failed_student(stu_set):
    if (60 <= stu_set["score"]):
        return True
    else:
        return False

gy_b = filter(pass_failed_student,gy_a)

print(list(gy_b))
 """

"""
3.19找出列表中最大数出现的位置
有个列表 a = [1, 2, 3, 11, 2, 5, 88, 3, 2, 5, 33]
找出列表中最大的数，出现的位置，下标从0开始
"""
""" 
gy_a = [1, 2, 3, 11, 2, 5, 88, 3, 2, 5, 33]
print(gy_a.index(max(gy_a)))
 """

"""
3.20找出列表中出现次数最多的元素
a = [
'my', 'skills', 'are', 'poor', 'I', 'am', 'poor', 'I',
'need', 'skills', 'more', 'my', 'ability', 'are',
'so', 'poor'
]
找出列表中出现次数最多的元素
"""
""" 
gy_a = [
'my', 'skills', 'are', 'poor', 'I', 'am', 'poor', 'I',
'need', 'skills', 'more', 'my', 'ability', 'are',
'so', 'poor'
]

gy_ch_count = 0
gy_ch_appear_max = ""
for gy_ch_i in gy_a:
    if (gy_ch_count < gy_a.count(gy_ch_i)):
        gy_ch_count = gy_a.count(gy_ch_i)
        gy_ch_appear_max = gy_ch_i

print(gy_ch_appear_max,gy_ch_count)

 """

"""
3.21分别统计列表中每个成员出现的次数
a = [
'my', 'skills', 'are', 'poor', 'I', 'am', 'poor', 'I',
'need', 'skills', 'more', 'my', 'ability', 'are',
'so', 'poor'
]
"""
""" 
gy_a = [
'my', 'skills', 'are', 'poor', 'I', 'am', 'poor', 'I',
'need', 'skills', 'more', 'my', 'ability', 'are',
'so', 'poor'
]

gy_dict = {}

for gy_ch_i in gy_a:
    gy_dict[gy_ch_i] = gy_a.count(gy_ch_i)

print(gy_dict)

a = [
'my', 'skills', 'are', 'poor', 'I', 'am', 'poor', 'I',
'need', 'skills', 'more', 'my', 'ability', 'are',
'so', 'poor'
]
rs={}
for i in a:
    if i not in rs.keys():
        rs[i]=1
    else:
        rs[i]+=1
print(rs)
 """

"""
3.22 列表查找元素位置
给定一个整数数组A及它的大小n，同时给定要查找的元素val，
请返回它在数组中的位置(从0开始)，若不存在该元素，返回-1。
若该元素出现多次请返回第一个找到的位置
如 A1=[1, "aa", 2, "bb", "val", 33]
或 A2 = [1, "aa", 2, "bb"]
"""
""" 
gy_A1 = [1, "aa", 2, "bb", "val", 33]
gy_A2 = [1, "aa", 2, "bb"]

def list_find(gy_list,find_val):
    if find_val in gy_list:
        return gy_list.index(find_val)
    else:
        return -1

print(list_find(gy_A1,"val"),list_find(gy_A2,"val"))

 """

"""
3.23列表查找两数之和
给定一个整数数组nums 和一个目标值target ，请你在该数组中找出和为目标值的那两个整数，并返回他
们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
示例:
给定nums=[2，7，11，15]，target=9
因为nums[0] + nums[1] =2+7 = 9
所以返回[0， 1]
"""
""" 
def find_add_index(gy_list,gy_sum):
    for gy_i in gy_list:
        for gy_j in gy_list:
            if (gy_sum == (gy_i + gy_j)):
                return [gy_list.index(gy_i),gy_list.index(gy_j)]
    else:
        return None

gy_nums = [2,3,4,5,4,5,9,3,1,4,0,8,3,4]
gy_target = 13

print(find_add_index(gy_nums,gy_target))
 """


"""
3.24二维数组取值(矩阵)
有 a = [["A", 1], ["B", 2]] ，如何取出 2
"""
""" 
gy_a = [["A", 1], ["B", 2]]

print(gy_a[1][1])
 """

"""
3.25 二维数组拼接
a = [[1,2],[3,4],[5,6]] 如何一句代码得到 [1, 2, 3, 4, 5, 6]
"""
""" 
gy_a = [[1,2],[3,4],[5,6]]

gy_b = [j for i in gy_a for j in i]

print(gy_b)

 """
"""
3.26 列表转字符串
L = [1, 2, 3, 5, 6]，如何得出 '12356'？
"""
""" 
gy_L = [1, 2, 3, 5, 6]
gy_str = ""
for gh_i in gy_L:
    gy_str += str(gh_i)

print(gy_str)
 """


"""
3.27 两个列表如何得到字典
a = ["a", "b", "c"]
b = [1, 2, 3]
如何得到 {'a': 1, 'b': 2, 'c': 3}
"""
""" 
gy_a = ["a", "b", "c"]
gy_b = [1, 2, 3]

gy_dict = {}

for gy_i in range(0,len(gy_a),1):
    gy_dict[gy_a[gy_i]] = gy_b[gy_i]

print(gy_dict)

gy_dict_1 = {gy_a[i]:gy_b[i] for i in range(0,len(gy_a),1)}
print(gy_dict_1)
 """

"""
.28列表按age从小到大排序
如下列表
people = [
{"name":"yoyo", "age": 20},
{"name":"admin", "age": 28},
{"name":"zhangsan", "age": 25},
]
按年龄age从小到大排序
"""
""" 
gy_persons = [
{"name":"yoyo", "age": 20},
{"name":"admin", "age": 28},
{"name":"zhangsan", "age": 25},
{"name":"garry", "age": 35},
{"name":"chili", "age": 33},
{"name":"vincent", "age": 45},
{"name":"ryan", "age": 35},
]

def get_age(gy_person):
    return gy_person["age"]

gy_persons_sortage = sorted(gy_persons,key = get_age,reverse = False)
print(gy_persons_sortage)


 """

"""
3.29列表插入元素
现有 nums=[2, 5, 7] ，如何在该数据最后插入一个数字 9 ，如何在2后面插入数字0
"""
""" 
gy_nums = [2,5,7]
gy_nums.append(9)
gy_nums.insert(1,0)
print(gy_nums)
 """


"""
3.30打乱列表顺序随机输出
有个列表a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
如何打乱列表a的顺序,每次得到一个无序列表
"""

gy_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(set(gy_a)))