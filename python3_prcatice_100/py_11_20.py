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

gy_string = "35143545345"

for gy_ch in gy_string:
    if ('0' > gy_ch) or ('9' < gy_ch):
        print("\"%s\" is not integer string !"%gy_string)
        break
else:
    print("\"%s\" is  integer string !"%gy_string)









