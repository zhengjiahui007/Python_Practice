"""
1.11 查找字符首次出现位置
输出指定字符串A在字符串B中第一次出现的位置，如果B中不包含A，则输出-1

从0开始计数
"""
""" 
gy_A = "hello"
gy_B = "hi how are you hello world, hello yoyo !"

gy_A_index = gy_B.find(gy_A)
if -1 != gy_A_index:
    print("The index of \"%s\" in \"%s\" is %d !"%(gy_A,gy_B,gy_A_index))
else:
    print("The \"%s\" is not in the \"%s\" !"%(gy_A,gy_B))
 """

"""
 1.12 查找字符串最后一次出现位置
输出指定字符串A在字符串B中最后出现的位置，如果B中不包含A，则输出-1

从0开始计数
"""

""" 
gy_A = "hllo"
gy_B = "hi how hell you hello world, hello yoyo hello odf !"


gy_B_temp = gy_B
gy_A_len = len(gy_A)
print("gy_A_len is %d !"%gy_A_len)
gy_A_index = gy_B_temp.find(gy_A)
while -1 != gy_A_index:
    gy_A_index_record = gy_A_index
    print("gy_A_index is %d !"%gy_A_index)
    gy_A_index = gy_B_temp.find(gy_A,gy_A_index + gy_A_len)
    if -1 == gy_A_index:
        print(gy_A_index_record)
        break
else:
    print(-1)
 """

"""
  1.13判断奇数偶数
　给定一个数a，判断一个数字是否为奇数或偶数
"""
""" 
gy_int_str = input("Please in input an integer : ")
gy_int = int(gy_int_str)

if 0 == (gy_int%2):
    print("%d is even number !"%gy_int)
else:
    print("%d is odd number !"%gy_int)

"""



"""
1.14判断一个姓名是否姓王
　输入一个姓名，判断是否姓王
 
"""

""" 
gy_name = "天王老五"

if "王" == gy_name[0]:
    print("姓王")
else:
    print("不姓王")
 """

""" 
1.15 判断是不是数字
如何判断一个字符串是不是纯数字组成
"""
""" 
gy_string = "35143545345"

for gy_ch in gy_string:
    if ('0' > gy_ch) or ('9' < gy_ch):
        print("\"%s\" is not integer string !"%gy_string)
        break
else:
    print("\"%s\" is  integer string !"%gy_string)

gy_string = "3o5143545345"
if gy_string.isdigit():
    print("\"%s\" is an integer string !"%gy_string)
else:
    print("\"%s\" is not an integer string !"%gy_string)

 """
"""
1.16 字符串大小写转换
将字符串 a="This is string example....wow!" 全部转成大写

字符串 b="Welcome To My World"全部转成小写

"""

# Answer
""" 
gy_str_a = "This is string example...wow!"
gy_str_b = "Welcome To My World"

print(gy_str_a.lower())
print(gy_str_b.upper())
 """

"""
1.17 字符串去掉首尾空格
将字符串a=" welcome to my world "首尾空格去掉
"""
#gy_a = "  welcome to my world    "
#print(gy_a)
#print(gy_a.strip())

"""
1.18字符串去掉左边指定空格或字符
1.19字符串去掉右边指定空格或字符
1.20 去除字符串里面所有的空格
"""
""" 
gy_str_a = "  Welcome to my world! "
print(gy_str_a)
print(gy_str_a.lstrip())

gy_str_b = "  Welcome to my world! "
print(gy_str_b)
print(gy_str_b.lstrip())

gy_str_c = "  Welcome to my world! "
print(gy_str_c)
print(gy_str_c.replace(" ",""))
 """

"""
1.21字符串去重后排序
s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
"""
""" 
gy_str_s = "ajldjlajfdljfddd"
gy_dict = {}
for gy_ch in gy_str_s:
    gy_ch_count = gy_str_s.count(gy_ch)
    gy_dict[gy_ch] = gy_ch_count

print(gy_dict)

gy_list = sorted(gy_dict.keys())
print(gy_list)
print("".join(gy_list))

gy_str_s = "ajldjlajfdljfddd"
gy_list = []

for gy_ch in gy_str_s:
    if gy_ch not in gy_list:
        gy_list.append(gy_ch)

print(gy_list)

print("".join(sorted(gy_list)))


 """

"""

1.22字符串去重保留顺序
s = "ajldjlajfdljfddd"，去重保留原来的顺序，输出"ajldf"
"""
""" 
gy_str_s = "ajldjlajfdljfddd"

gy_list_s = []

for gy_ch in gy_str_s:
    if gy_ch not in gy_list_s:
        gy_list_s.append(gy_ch)

print("".join(gy_list_s))
 """

"""
1.23画菱形
题目 打印出如下图案（菱形）:
"""

gy_N = 7
gy_line = 0
gy_row_star = 0
gy_row_space = 0

for gy_line in range(1,gy_N//2 + 2,1):
    for gy_row_space in range(1,gy_N//2 + 1 - gy_line,1):
        print(" ",end = "")
    
    for gy_row_star in range(1,2 * gy_line - 1 + 1,1):
        print("*",end = "")
    print("\n")

for gy_line in range(1,gy_N//2 + 1,1):
    for gy_row_space in range(1,gy_line + 1,1):
        print(" ",end = "")
    
    for gy_row_star in range(1,gy_N - 2 * gy_line + 1,1):
        print("*",end = "")
    print("\n")




"""
1.24 输入一个正整数，判断是几位数
题目 给一个不多于5位的正整数，要求：
一、求它是几位数，
二、逆序打印出各位数字。
a = 12345
"""
""" 
gy_int_str = input("Please input a positive integer no more than 5 digit: ")

if not gy_int_str.isdigit():
    print("The %s is not a integer!"%gy_int_str)
else:
    print("The %s is a %d digit integer !"%(gy_int_str,len(gy_int_str)))
    print(gy_int_str[::-1])

 """


















