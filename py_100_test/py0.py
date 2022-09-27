'''
Practic 1
numbers = [2,4,6,8,18]

for k in numbers:
    if k % 2 == 0:
        print(k)
        #break;
    else:
        print("NO odd number!")

print("************************************")
number1 = (12,14,16,18,118)
for k in number1:
    if k % 2 == 0:
        print(k)
        #break;
    else:
        print("NO odd number!")

print("************************************")
number2 = {12,14,16,18,118}
for k in number2:
    if k % 2 == 0:
        print(k)
        #break;
    else:
        print("NO odd number!")

print("************************************")
number3 = {12:13,14:15,16:17,18:19,118:119}
for k in number3:
    if k % 2 == 0:
        print(k)
        #break;
    else:
        print("NO odd number!")
'''

'''
#Practice 2 从列表中获取元素，定义多个变量
my_list = [5,8,3,45,5]
one,two,three,four,five = my_list
print(one)
print(two)
print(three)
print(four)
print(five)
'''

'''
#Practice 3 使用heapq模块，获取列表中n个最大或最小的元素
import heapq
scores = [51,33,64,87,91,75,15,49,33,82]

print(heapq.nlargest(3,scores))
print(heapq.nsmallest(5,scores))
'''

#Practice 4 将列表中的所有元素作为参数传递给函数
'''
my_list = [5,8,3,45,5]
print(my_list)
print(*my_list)
print(type(my_list))

def my_printf(*para):
    print(para)


my_printf(1,2,3)

def sum_of_elements(arg):
    total = 0
    for i in arg:
        total += i

    return total

result = sum_of_elements(my_list)
print(result)
'''

'''
print(type([]))
print(type({}))
print(type(set()))

print(type([1,2]))
print(type({1:3,2:4}))
print(type((1,2,3)))
print(type({1,2,3}))
'''

#Practice5、获取列表的所有中间元素
'''
_,*list_my,_ = [1,2,3,4,5,6,7]
_,*tuple_my,_ = (9,8,7,6,5,4)
_,*set_my,_ = {6,8,5,4,9,77}
_,*dict_my,_ = {'A':1,'B':2,'C':3,'D':4}

print(list_my)
print(tuple_my)
print(set_my)
print(dict_my)
'''

#Practice6、使用一行代码赋值多个变量
one_my,two_my,three_my,four_my = 1,5,6,9

print(one_my)
print(two_my)
print(three_my)
print(four_my)


