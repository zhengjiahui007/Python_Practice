
# list_original = [1,2,3,4,5,7,8,9]
# print(list_original)

# name_list = list("pythonkl")
# print(name_list)

# #等长替换 直接替换
# name_list[2:4] = ['b','x']
# print(name_list)

# #不等长替换 多的补上
# name_list = list("pythonkl")
# print(name_list)
# name_list[5:] = ['b','x','b','x','b','x']
# print(name_list)

# #不等长在中间替换 把原位置替换，后面多的补上
# name_list = list("pythonkl")
# print(name_list)
# name_list[2:4] = ['b','x','b','x']
# print(name_list)

# #替换的list比原list要短
# name_list = list("pythonkl")
# print(name_list)
# name_list[2:] = ['b','x']
# print(name_list)

# #替换的list比原list要短
# name_list = list("pythonkl")
# print(name_list)
# name_list[2:6] = ['b','x']
# print(name_list)

#空切片,列表赋值给空切片
# name_list = list("pythonkl")
# print(name_list)
# print(name_list[2:2:1])
# print(name_list[2::1])
# print(name_list[::1])
# print(name_list[-1::1])
# print(name_list[:0:1])

# name_list[2:2] = ['b','c','e']
# print(name_list)

#空切片赋值给切片
name_list = list("pythonkl")
print(name_list)
name_list[2:5] = []
print(name_list)




'''
切片的用法object[start_index : end_index : step]:
如果没有缺省的话，表达式应该包含三个参数以及两个冒号，三个参数的意义分别如下：
1、start_index：切片的起始位置(包括该位置)，0表示从第一个开始，1表示从第二个开始，以此类推。
-1表示从倒数第一个开始，-2表示从倒数第二个开始，以此类推。
缺省时取0或-1(即step为正数取0，负数取-1)a=[9,2,8,7,4,5,1,5,6,8]

1、start_index：切片的起始位置(包括该位置)，0表示从第一个开始，1表示从第二个开始，以此类推。-1表示从倒数第一个开始，-2表示从倒数第二个开始，以此类推。缺省时取0或-1(即step为正数取0，负数取-1)a=[9,2,8,7,4,5,1,5,6,8]

a[0::]表示从第一个到最后一个,结果为  #[9，2，8，7，4，5，1，5，6，8]

a[1::]表示从第二个到最后一个          #[2，8，7，4，5，1，5，6，8]

a[-1::]表示从最后一个到最后一个，一共取一个值  #[8]

2、end_index：切片的结束位置(！！！且不包括该位置)，0表示第一个为终点，1表示第二个为终点，以此类推。-1表示倒数第一个为终点，-2表示倒数第二个为终点，以此类推。缺省时默认为序列长度(step为正数取正，step负数取负)a=[9,2,8,7,4,5,1,5,6,8]

a[:0:]表示从第一个到第一个，一共取0个值      #[]

a[:1:]表示从第一个到第二个且不包括第二个     #[9]

a[:-1:]表示从第一个到最后一个且不包括最后一个，一共取9个值      #[9，2，8，7，4，5，1，5，6]

a[:8]表示从第一个到第九个且不包括第九个      #[9, 2, 8, 7, 4, 5, 1, 5]

3、step，表示步长。可取正负数，正数表示从左往右，负数表示从右往左。缺省时取1a=[9,2,8,7,4,5,1,5,6,8]

a[::1]表示从第一个到最后一个，步长为1      #[9，2，8，7，4，5，1，5，6，8]

a[::-1]表示从最后一个到第一个，步长为1       #[9，6，5，1，5，4，7，8，2，9]

a[::2]表示从第一个到最后一个，步长为2         #[9，8，4，1，6]


'''