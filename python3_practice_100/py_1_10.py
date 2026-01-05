'''
第1章 字符串练习题
1.1交换
已知a的值为“hello”,b的值为“world”,如何交换a和b的值?
得到a的值为“world”,b的值为“hello”
'''
# Answer : 

""" a = "Hello"
b = "World"
print("a is " + a + " and b is " + b)
a,b = b,a
print("Now a is " + a + " and b is " + b)
# format : https://blog.csdn.net/weixin_37988176/article/details/109376909
print("a is {} b is {} ".format(a,b))
 """

"""
1.2回文
回文的定义：“回文”就是正读倒读都是一样的

如奇数个“98789”，这个数字正读是“98789”倒读也是“98789”。

偶数个数字“3223”也是回文数。

字母“abcba”也是回文。

判断一个字符串是否是回文字符串，是打印True，不是打印False。
"""
# Answer 
"""
def Judge_String_Huiwen(str):
    
    Hui_wen_flag = True
    for i in range(0,len(str) // 2):
        if str[i] != str[len(str) - i - 1]:
            Hui_wen_flag = False
            break

    return Hui_wen_flag

print("Please input a string : ")
a_str = input()
a_result = Judge_String_Huiwen(a_str)
if a_result:
    print("True {} is Huiwen !".format(a_str))
else:
    print("False %s is not Huiwen !"%a_str)

 """
""" #print("Please input a string : ")
a_str = input("Please input a string : ")

a_str_rever = a_str[::-1]

if a_str_rever == a_str:
    print("True \"{}\" is Huiwen !".format(a_str))
else:
    print("False \"%s\" is not Huiwen !"%a_str) """



""" 
1.3字符串切割
已知一个字符串为“hello_world_huihui”，如何得到一个队列["hello","world","huihui"]
"""

"""  #Answer : 
a = 'hello_world_huihui'
b = a.split('_')
print(b) """

"""
 1.4拼接字符串
有个列表['hello', 'world', 'huihui']　如何把列表里的字符串串联起来

得到字符串"hello_world_huihui
"""

#Answer : 
""" 
gy_list = ['hello','world','huihui']
gy_string = gy_list[0]
#for i in range(1,len(gy_list)):
    #gy_string += ('_' + gy_list[i])
print(gy_list[1:])
for i in gy_list[1:]:
    gy_string += ('_' + i)

print(gy_string)
gy_string = ""
print(gy_list[0:-1])
for i in gy_list[0:-1]:
    gy_string += (i + "_")

gy_string += gy_list[-1]

print(gy_string)

gy_list_1 = ['hello','world','huihui']
gy_string_1 = ""

for i in gy_list_1:
    gy_string_1 += i
    gy_string_1 += '_'

print(gy_string_1) """

"""
1.5 替换字符
把字符串s中的每个空格替换成"%20"

输入：s="We are happy."

输出："We%20are%20happy."
"""

#Answer : 

""" gy_str = "We are happy."

gy_str_1 = gy_str.replace(" ","%20")
print(gy_str + "\n" + gy_str_1) """

"""
1.6 九九乘法表
打印99乘法表
"""

""" #Answer : 
for x in range(1,10,1):
    for y in range(1,x + 1,1):
        if((x * y) < 10):
            print("%d * %d = %d"%(y,x,x*y),end = "  | ")
        else:
            print("%d * %d = %d"%(y,x,x*y),end = " | ")
        #print("{} * {} = {}".format(y,x,y * x),end = " | ")
    print(end = "\n") """

"""
1.7字符下标
找出单词"welcome"　在字符串"Hello,welcome." 中出现的位置，找不到返回-1

从下标0开始索引
"""

""" #Answer : 
gy_string = "Hello,welcome."

print(gy_string.find("welco0me"))

gy_list = ['hello','world','huihui']

gy_join = "_"
gy_join_str = gy_join.join(gy_list)
print(gy_join_str) """

"""
　1.8 统计字符出现的次数
统计字符串"Hello,welcome to my world."　中字母w出现的次数

统计单词my出现的次数
"""
""" 
gy_string = "Helwetgo,welcome we mywweworld."
gy_str_sub = "w"

gy_count_sub = 0

gy_str_sub_len = len(gy_str_sub)
gy_string_len  = len(gy_string)
print("gy_string_len is " + str(gy_string_len) + ", gy_str_sub_len is " + str(gy_str_sub_len))

#if gy_str_sub in gy_string:
gy_string_temp = gy_string
gy_count_sub = 0
gy_sub_index = gy_string_temp.find(gy_str_sub)

while -1 != gy_sub_index:
    gy_count_sub += 1
    #print(gy_string_temp)
    gy_string_temp = gy_string_temp[gy_sub_index + gy_str_sub_len::]
    #print(gy_string_temp)
    gy_sub_index = gy_string_temp.find(gy_str_sub)
    #print(gy_sub_index)

print("The number of \"%s\" in \"%s\" is %d !"%(gy_str_sub,gy_string,gy_count_sub))


while gy_str_sub in gy_string_temp:
    gy_count_sub += 1
    gy_sub_index = gy_string_temp.find(gy_str_sub)
    gy_string_temp = gy_string_temp[gy_sub_index + gy_str_sub_len::]

print("The number of \"%s\" in \"%s\" is %d !"%(gy_str_sub,gy_string,gy_count_sub))
#print(gy_string[0:3:1]) """
"""
gy_count_sub   = 0
gy_str_sub_len = len(gy_str_sub)
gy_string_len  = len(gy_string)
print("gy_string_len is " + str(gy_string_len) + ", gy_str_sub_len is " + str(gy_str_sub_len))

print("method 1 : ")
gy_list_string = []
#print(type(gy_list_string))
for i in range(0,gy_string_len//gy_str_sub_len,1):
    #print(gy_string[(i * gy_str_sub_len) : (i * gy_str_sub_len + gy_str_sub_len) : 1])
    gy_list_string.append(gy_string[(i * gy_str_sub_len) : (i * gy_str_sub_len + gy_str_sub_len) : 1])

print(gy_list_string)
gy_count_sub = 0
for i in gy_list_string:
    if (i == gy_str_sub):
        gy_count_sub += 1

#print("The number of {} in {} is {} !".format(gy_str_sub,gy_string,gy_count_sub))
print("The number of \"%s\" in \"%s\" is %d !"%(gy_str_sub,gy_string,gy_count_sub))

print("method 2 : ")
gy_count_sub = 0
for i in range(0,gy_string_len,gy_str_sub_len):
    #print(i)
    print(gy_string[i:i + gy_str_sub_len:1],end = " ")
    if gy_string[i:i + gy_str_sub_len:1] == gy_str_sub:
        gy_count_sub += 1

print("\nThe number of \"%s\" in \"%s\" is %d !"%(gy_str_sub,gy_string,gy_count_sub))
"""

"""
1.9 统计每个字符出现的次数
题目：输入一个字符串str，输出第m个只出现过n次的字符，　如在字符串gbgkkdehh中，找出第2个只出现1次的字符，输出结果：d

"""

#Answer : 
""" 
gy_string = "ertgfddgdegdafdffddfdde"
gy_m_th = 2
gy_n_appear_times = 3
gy_dict = {}

for gy_ch_i in gy_string:
    gy_appear_count = 0
    for gy_ch_j in gy_string:
        if gy_ch_i == gy_ch_j:
            gy_appear_count += 1
    gy_dict[gy_ch_i] = gy_appear_count

print(gy_dict)

gy_appear_times = 0
for gy_dict_item in gy_dict.items():
    if gy_n_appear_times == gy_dict_item[1]:
        gy_appear_times += 1
        if gy_m_th == gy_appear_times:
            print("The \"%s\" is the %d character appearing %d times!"%(gy_dict_item[0],gy_m_th,gy_n_appear_times))
            break
else:
    print("There is no character matching the condition!")
 """

"""
 1.10 判断字符a含b
判断字符串a="welcome to my world" 是否包含单词b="world"，包含返回True，不包含返回False
"""
""" 
gy_a = "welcome to my world"
gy_b = "world"

if gy_b in gy_a:
    print("True")
else:
    print("False")
 """