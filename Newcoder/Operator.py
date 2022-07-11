import inspect

file_name = inspect.currentframe()

# #NP6
# # 使用print()语句直接打印数字2和数字3是否相等的比较结果；
# print(str(file_name.f_lineno) + " : " + str(2 == 3))

# # 使用print()语句直接打印数字2和数字3是否不相等的比较结果；
# print(str(file_name.f_lineno) + " : " + str(2 != 3))

# # 使用print()语句直接打印数字2是否大于数字3的比较结果；
# print(str(file_name.f_lineno) + " : " + str(2 > 3))

# # 使用print()语句直接打印数字2是否小于数字3的比较结果；
# print(str(file_name.f_lineno) + " : " + str(2 < 3))

# # 使用print()语句直接打印数字2是否大于等于数字3的比较结果；
# print(str(file_name.f_lineno) + " : " + str(2 >= 3))

# # 使用print()语句直接打印数字2是否小于等于数字3的比较结果；
# print(str(file_name.f_lineno) + " : " + str(2 <= 3))

# # 使用print()语句直接打印 数字2是否小于数字3的比较结果 逻辑与（也即使用 and 运算符） 数字2是否小于数字1的比较结果 的运算结果 ；
# print(str(file_name.f_lineno) + " : " + str((2 < 3) and (2 < 1)))

# # 使用print()语句直接打印 数字2是否小于数字3的比较结果 逻辑或（也即使用 or 运算符） 数字2是否小于数字1 的比较结果 的运算结果；
# print(str(file_name.f_lineno) + " : " + str((2 < 3) or (2 < 1)))

# # 使用print()语句直接打印字符串'Python'和字符串"Python"是否相等的比较结果；
# print(str(file_name.f_lineno) + " : " + str('Python' == "Python"))

# # 使用print()语句直接打印字符串'Python2'和字符串'Python3'是否不相等的比较结果；
# print(str(file_name.f_lineno) + " : " + str('Python2' != 'Python3'))

# # 使用print()语句直接打印字符串'PYTHON'.lower()和字符串'Python'.lower()是否相等的比较结果；
# print(str(file_name.f_lineno) + " : " + str('PYTHON'.lower() == 'Python'.lower()))

# # 创建一个列表my_list，其中依次包含[1, 3]中的所有整数，
# my_list = [1,2,3]

# # 如果数字2在列表my_list里，请使用print()语句一行打印字符串'2 is in my_list!'；
# if 2 in my_list:
#     print("2 is in my_list!")

# # 如果数字8不在列表my_list里，请使用print()语句一行打印字符串'8 is not in my_list!'。
# if 8 not in my_list:
#     print("8 is not in my_list!")

#NP7
# 这个计算器要实现的功能包括：
# 读入第一个数字记入变量x中，读入第二个数字记入变量y中；
# 然后依次逐行用print函数打印x与y相加，x减去y，x与y相乘，x除以y（整除），x对y取余的计算结果。
# 输入描述：
# 输入两个整数，x与y，其中y不会为0

def caculator(x,y):
    if 0 == y:
        print("y is zero,wrong!")
        return None
    
    print("%d + %d =  " %(x,y),x + y)
    print("%d - %d =  " %(x,y),x - y)
    print("%d * %d =  " %(x,y),x*y)
    print("%d / %d =  " %(x,y),x/y)
    print("%d %% %d =  " %(x,y),x%y)
    print("%d // %d =  " %(x,y),x//y)
    print("%d ** %d =  " %(x,y),x**y)
    return None

x_para = input()
y_para = input()
caculator(int(x_para),int(y_para))
