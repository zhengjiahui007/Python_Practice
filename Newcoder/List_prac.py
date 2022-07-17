#NP8
# offer_list = ["Allen","Tom","Garry"]

# for i_name in offer_list:
#     print(i_name + ", you have passed our interview and will soon become a member of our company.")

# offer_list[1] = "Andy"

# for i_name in offer_list:
#     print("%s , wellcom to join to us !" %i_name)

# offer_list.insert(2,"Zheng")
# for i_name in offer_list:
#     print("%s , wellcom to join to us !" %i_name)

#NP9
'''
描述
为庆祝驼瑞驰在牛爱网找到合适的对象，所以驼瑞驰创建了一个依次包含字符串 'Niuniu' 和 'Niu Ke Le' 的列表guest_list，作为庆祝派对的邀请名单。
请你依次对列表中的名字发送类似'Niuniu, do you want to come to my celebration party?'的句子。
驼瑞驰的好朋友牛牛、GURR哥和LOLO姐也正好有空，所以请使用insert()方法把字符串'GURR'插入到列表guest_list的开头，
再使用insert()方法把字符串'Niumei'插入到字符串'Niu Ke Le'的前面，再使用append()方法把字符串'LOLO'插入到列表guest_list的最后，
再依次发送类似'Niuniu, thank you for coming to my celebration party!'的句子。
'''

# guest_list = ["Niuniu","Nui Ke Le"]

# for guest_name in guest_list:
#     print(guest_name + ", do you want to come to my celebration party?")

# guest_list.insert(0,"GURR")
# index_niukele = guest_list.index("Nui Ke Le")
# print("The index of Niu Ke Le is %d" %index_niukele)
# guest_list.insert(index_niukele,"Niumei")
# guest_list.append("LOLO")

# print("***********************************")
# for guest_name in guest_list:
#     print(guest_name + ", thank you for coming to my celebration party!")

'''
NP10
毕业季到了，牛牛为了找工作准备了自己简历，以及投递公司的列表company_list，其中包括了字符串 'Alibaba', 'Baidu', 'Tencent', 'MeiTuan', 'JD' 作为他投递简历的目标公司。
请向列表中每个公司发送一条消息类似 'Hello Alibaba, here is my resume!'。
然而，遗憾的是Alibaba、Tencent、MeiTuan、JD都没有通过牛牛的简历审核，只有Baidu回复了他，邀请他去参加面试。因此你需要：
使用 del() 函数删除列表company_list中的字符串 'Alibaba'.
使用 pop() 函数依次删除列表company_list中的字符串'JD'，'MeiTuan'.
使用 remove() 函数删除列表company_list中的字符串'Tencent'.
最后向列表中的剩余的公司发送类似 'Baidu, thank you for passing my resume. I will attend the interview on time!' 的消息。

'''

# company_list = ["Alibaba","Baidu","Tencent","MeiTuan","JD"]

# for company_name in company_list:
#     print("Hello %s , here is my resume !" %company_name)

# del company_list[0]
# company_list.pop(-1)
# company_list.pop(-1)
# company_list.remove("Tencent")

# for company_name in company_list:
#     print("%s , thank you for passing my resume. I will attend the interview on time !" %company_name)

'''
NP11
创建一个依次包含字符串'P'、'y'、't'、'h'、'o'和'n'的列表my_list后，
先使用print()语句一行打印字符串'Here is the original list:'，再直接使用print()语句把刚刚创建的列表my_list整个打印出来，

输出一个换行，再使用print()语句一行打印字符串'The result of a temporary reverse order:'，
再使用print()语句把使用sorted()函数对列表my_list进行临时降序排序的结果整个打印出来；

输出一个换行，再使用print()语句一行打印字符串'Here is the original list again:'，
再使用print()语句把原来的列表my_list整个打印出来，确认没有改变原来的列表my_list；

对列表my_list调用sort()方法，使列表my_list中的字符串以降序排序，
输出一个换行，再使用print()语句一行打印字符串'The list was changed to:'，
再使用print()语句把修改后的列表my_list整个打印出来，确认列表my_list的字符串以降序排序；

对列表my_list调用reverse()方法，使列表my_list中的字符串的位置前后翻转，
输出一个换行，再使用print()语句一行打印字符串'The list was changed to:'，
再使用print()语句把修改后的列表my_list整个打印出来，确认列表my_list的字符串的位置前后翻转了。
'''

# test_list = ['P','y','t','h','o','n']
# print('Here is the original list : ')
# print(test_list)
# print()

# print('The result of a temporary reverse order : ')
# reverse_list = sorted(test_list,reverse = True)
# print(reverse_list)
# print()

# print('Here is the original list again : ')
# print(test_list)
# print()

# test_list.sort(reverse = True)
# print('The list was changed to : ')
# print(test_list)
# print()

# test_list.reverse()
# print('The list was changed to : ')
# print(test_list)

#NP12
'''
使用一个 for 循环 或 while 循环 打印[1, 20]中的所有整数（一行一个数字）。
'''

# num_list = range(1,21,1)
# for k in num_list:
#     print(k)

'''
NP13
牛牛有一个name = ['Niumei', 'YOLO', 'Niu Ke Le', 'Mona'] 记录了他最好的朋友们的名字，请创建一个二维列表friends，
使用append函数将name添加到friends的第一行。
假如Niumei最喜欢吃pizza，最喜欢数字3，YOLO最喜欢吃fish， 最喜欢数字6，Niu Ke Le最喜欢吃potato，最喜欢数字0，
Mona最喜欢吃beef，最喜欢数字3。
请再次创建一个列表food依次记录朋友们最喜欢吃的食物，并将创建好的列表使用append函数添加到friends的第二行；
然后再创建一个列表number依次记录朋友们最喜欢的颜色，并将创建好的列表使用append函数添加到friends的第三行。
这样friends就是一个二维list，使用print函数直接打印这个二维list。
输入描述：
'''

#print(type([[]]))
# print(type(()))
# print(type({}))

# print(type(set()))

# name_friends = ["Nuimei","YOLO","Niu Ke Le","Mona"]
# List_friends = []
# print(List_friends)
# List_friends.append(name_friends)
# print(List_friends)
# food_friends = ["pizza","fish","potato","beef"]
# List_friends.append(food_friends)
# print(List_friends)
# numbers_friends = [3,6,0,3]
# List_friends.append(numbers_friends)
# print(List_friends)