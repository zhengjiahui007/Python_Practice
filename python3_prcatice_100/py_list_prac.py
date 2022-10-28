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
