
'''
NP14
创建一个依次包含字符串'P'、'y'、't'、'h'、'o'和'n'的列表my_list，
使用print()语句一行打印字符串'Here is the original list:'，再直接使用print()语句把刚刚创建的列表my_list整个打印出来，
输出一个换行，再使用print()语句一行打印字符串'The number that my_list has is:'，
再使用len()函数获取列表my_list里面有多少个字符串，并使用print()函数一行打印该整数。

'''

# my_list = ['P','y','t','h','o','n']
# print("Here is the orginal list : ")
# print(my_list)
# print(" ")
# print("The number that my_list has is : %d !"  %len(my_list))

'''
NP15
牛牛、牛妹和牛可乐都是Nowcoder的忠实用户，又到了一年一度的程序员节（10月24号），毫无疑问，
他们都登录Nowcoder了，因为他们还没有刷完牛客题霸...
Nowcoder的管理员想对他们发送一些简单登录问候消息，并对他们表达了节日祝福。
请创建一个依次包含字符串 'Niuniu' 、'Niumei' 和 'Niu Ke Le' 的列表users_list，
请使用for循环遍历列表user_list，依次对列表users_list中的名字输出一行类似 
'Hi, Niuniu! Welcome to Nowcoder!' 的字符串，
for循环结束后，最后输出一行字符串 "Happy Programmers' Day to everyone!"

'''

# user_list = ["Niuniu","Niumei","Niu Ke Le"]

# for user_name in user_list:
#     print("Hi,%s ! Welcome to Newcoder !" %user_name)

# print("Happy Programmers' Day to everyone !")

'''
NP16
创建一个列表my_list，其中包含[1, 1 000]中的所有整数，
再使用 min() 和 max() 核实该列表确实是从 1 开始，到 1 000 结束的。
此外，再对这个列表调用函数 sum()，看看 Python 将这一千个数字相加得到的结果是多少。
最后，对这个列表的所有整数求取平均值，直接保留一位小数。
'''

# my_number_list = range(1,1000 + 1,1)
# print(min(my_number_list))
# print(max(my_number_list))
# print(len(my_number_list))
# print(sum(my_number_list))
# aver = 0.0
# aver = sum(my_number_list)/len(my_number_list)
# print("Average is  %.3f ." %(sum(my_number_list)/len(my_number_list)))

'''
NP17
通过给函数 range()指定第三个参数来创建一个列表my_list，其中包含 [0, 19]  中的所有偶数；
再使用一个 for 循环将这些数字都打印出来（每个数字独占一行）。
'''

# my_list_even = range(0,19 + 1,2)
# for k_even in my_list_even:
#     print(k_even)

'''
N18
创建一个列表my_list，其中包括 [1, 50] 内全部能被5整除的数字；
再使用一个 for 循环将这个列表中的数字都打印出来（每个数字独占一行）。
'''

# my_list_5 = range(1,50 + 1,1)
# for k_5 in my_list_5:
#     if(0 == (k_5 % 5)):
#         print(k_5)

'''
NP19
在Python中， * 代表乘法运算， ** 代表次方运算。
请创建一个空列表my_list，使用for循环、range()函数和append()函数令列表my_list包含底数2的 [1, 10] 次方，
再使用一个 for 循环将这些次方数都打印出来（每个数字独占一行）。
'''

# my_list_2powder = []
# for k in range(1,10 + 1,1):
#     my_list_2powder.append(2 ** k)

# for k in my_list_2powder:
#     print(k)

'''
NP20
使用列表解析生成一个列表my_list，其中包含前 10 个整数（也即[1, 10]）的立方。
再直接使用print()语句把刚刚创建的列表my_list整个打印出来（以列表形式，也即两边带方括号）。
'''

my_list_cubic = []

for k in range(1,10 + 1,1):
    my_list_cubic.append(k ** 3)

print(my_list_cubic)

'''
NP21
创建一个列表group_list，其中依次包含字符串 'Tom', 'Allen', 'Jane', 'William', 'Tony' 表示这个小组成员的名字。
现有三项任务需要他们去完成，根据不同任务的繁琐度和实际情况需要分别派2人、3人、2人来完成，他们决定通过对列表分片来分配任务。
使用print()语句和切片来打印列表group_list的前两个元素表示去做第一个任务的人的名字，
再使用print()语句和切片来打印列表group_list的中间三个元素表示去做第二个任务的人的名字，
再使用print()语句和切片来打印列表group_list的后两个元素表示去做第三个任务的人的名字
'''

group_name_list = ['Tom','Allen','Jane','Willam','Tony']
print(group_name_list[0:2])
print(group_name_list[1:4])
print(group_name_list[-2:])
print(group_name_list[1:1])