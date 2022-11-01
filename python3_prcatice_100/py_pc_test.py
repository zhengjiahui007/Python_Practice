"""
5.1 有1、2、3、4组成无重复数的三位数（排列组合）
有1、2、3、4数字能组成多少互不相同无重复数的三位数?
分别打印这些三位数的组合
"""
""" 
gy_N = [1,2,3,4]
gy_integer = []

for gy_i_100 in gy_N:
    gy_sum = gy_i_100 * 100
    for gy_i_10 in gy_N:
        if (gy_i_100 != gy_i_10):
            gy_sum = gy_i_100 * 100 + gy_i_10 * 10
            for gy_i_1 in gy_N:
                if ((gy_i_1 != gy_i_10) and (gy_i_1 != gy_i_100)):
                    gy_sum = gy_i_100 * 100 + gy_i_10 * 10 + gy_i_1 * 1
                    gy_integer.append(gy_sum)

print(gy_integer)
print(len(gy_integer))

gy_int_list = []

for gy_i in range(0,len(gy_N),1):
    gy_N_temp = gy_N.copy()
    del gy_N_temp[gy_i]
    for gy_j in range(0,len(gy_N_temp),1):
        gy_N_temp_1 = gy_N_temp.copy()
        del gy_N_temp_1[gy_j]
        for gy_k in range(0,len(gy_N_temp_1),1):
            gy_int_list.append(gy_N[gy_i]*100 + gy_N_temp[gy_j]*10 + gy_N_temp_1[gy_k])

print(gy_int_list)
print(len(gy_int_list))

 """

"""
5.2 冒泡排序
a = [11, 2, 33, 1, 5, 88, 3]

冒泡排序：
依次比较两个相邻的元素，如果顺序（如从小到大、首字母从A到Z）
错误就把他们交换过来
"""
""" 
gy_a = [11, 2, 33, 1, 5, 88, 3]

for k in range(0,len(gy_a),1):
    for j in range(k + 1,len(gy_a),1):
        if (gy_a[k] < gy_a[j]):
            gy_a[k],gy_a[j] = gy_a[j],gy_a[k]

print(gy_a)

gy_a = [11, 2, 33, 1, 5, 88, 3]
for k in range(0,len(gy_a),1):
    for j in range(k + 1,len(gy_a),1):
        if (gy_a[k] > gy_a[j]):
            gy_a[j],gy_a[k] = gy_a[k],gy_a[j]

print(gy_a)

gy_a = [11, 2, 33, 1, 5, 88, 3]
print(sorted(gy_a,reverse = False))
print(sorted(gy_a,reverse = True))

 """

"""
5.3文本中每行中长度超过3的单词
在以下文本中找出 每行中长度超过3的单词:
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick

python的预期结果(尽量不超过3行搞定):
[['Call', 'Ishmael.', 'Some', 'years', 'never', 'mind', 'long', 'precisely', 'having'],
['little', 'money', 'purse,', 'nothing', 'particular', 'interest'],
['shore,', 'thought', 'would', 'sail', 'about', 'little', 'watery', 'part'],
['world.', 'have', 'driving', 'spleen,', 'regulating'],
['circulation.', 'Moby', 'Dick']]]
"""

gy_text = """Call me Ishmael. Some years ago - never mind how long precisely - having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen, and regulating the circulation. - Moby Dick"""

gy_text = """
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick
"""

#gy_text = gy_text.replace(","," ")
#gy_text = gy_text.replace("."," ")
#gy_text = gy_text.replace("\n"," ")
""" 
print(gy_text)

gy_text_list = gy_text.split("\n")

print(gy_text_list)

gy_words_morethan3 = [x for i in gy_text_list for x in i if 3 < len(x) ]

print(gy_words_morethan3)
 """
""" 
a=
"""
"""
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick
"""
"""
a=a.replace(',',' ')
a=a.replace('.',' ')
a=a.replace('\n',' ')
print(a)
a=a.split(" ")
print(a)
rs=[i for i in a if len(i)>3]
print(rs)
 """
#gy_list = [x for x in gy_text_1 if 3 < len(x)]

#print(gy_list)

#print(gy_text_1)


""" 
gy_text_list = gy_text.split("\n")
print(gy_text_list)

def str_len_morethan3(gy_str):
    if 3 < len(gy_str):
        return True
    else:
        return False

gy_list_words_morethan3 = []

for gy_str_i in gy_text_list:
    if 0 < len(gy_str_i):
        gy_list_line = gy_str_i.split(" ")
        #print(gy_list_line)
        gy_list_words_morethan3.append(list(filter(str_len_morethan3,gy_list_line)))

print(gy_list_words_morethan3)

 """


"""
5.4 列表数据写入txt（open读写）
有一个数据list of dict如下
a = [
{"yoyo1": "123456"},
{"yoyo2": "123456"},
{"yoyo3": "123456"},
]
写入到本地一个txt文件，内容格式如下：
yoyo1,123456
yoyo2,123456
yoyo3,123456
"""


"""
5.7 计算纯数字子串组成的单一数字（子串）
有一个纯数字组成的字符串, 返回连续单一数字子串的个数
输入字符串： “22252”
只含单一数字的子串是
1个字符：2出现4次，5出现1次
2个字符 22 出现2 次
3个字符 222 出现1 次
4个子串 0次
5个字符 0次
总共 4+1+2+1 =8
输出结果：8
"""
""" 
print("22252".count("22"))

gy_string = input("Please input a string with all integer : ")


if gy_string.isdigit():
    pass
else:
    print("It is not a digital string !")

gy_dict = {}

def judge_string_have_thesamedigit(gy_str,length):
    first_str = gy_str[0]
    if (gy_str.count(first_str) == length):
        return True
    else:
        return False
gy_sub_samedigit = 0
for gy_k in range(1,len(gy_string) + 1,1):
    for gy_m in range(0,len(gy_string) + 1 - gy_k,1):
       gy_str_sub = gy_string[gy_m:(gy_m + gy_k):1]
       if judge_string_have_thesamedigit(gy_str_sub,len(gy_str_sub)):
            print(gy_str_sub,gy_string.count(gy_str_sub))
            #gy_dict[gy_str_sub] = gy_string.count(gy_str_sub)
            gy_sub_samedigit += 1

print(gy_sub_samedigit)
 """

""" 
def nums(n):
    print(set(n))
    onlyn=list(set(n))
    print(onlyn)
    count=0
    for i in onlyn:
        for j in range(1,len(n)+1): #字符个数
            for k in range(len(n)):
                if n[k:k+j]==i*j:
                    count+=1
    return count
a="22252"
print(nums(a))
def nums(s):
    count=0
    for i in range(len(s)):
        count+=1
        for j in range(i+1,len(s)):
            if s[j]==s[i]: #与i相当，则说明数字在重复
                count+=1
            else:
                break
    return count
print(nums('22252'))
 """

"""
5.8 移除字符串里面的'ab'
有一个字符串列表['aababbc', 'badabcab'] 将字符串中的'ab' 移除
比如'aababbc' 移除里面的ab后得到abc 需继续移除ab，得到c，直到字符串中不会出现连续的ab
"""

#gy_string = ['aababbc','badabcab']

""" 
def gy_remove_substr(string_orig,sub_str):
    sub_str_len = len(sub_str)
    string_temp = string_orig
    while (sub_str in string_temp):
        sub_str_index = string_temp.find(sub_str)
        string_temp = string_temp[0:sub_str_index:1] + string_temp[sub_str_index + sub_str_len::1]
    else:
        return string_temp

print(gy_remove_substr(gy_string[0],'ab'))
print(gy_remove_substr(gy_string[1],'ab'))

 """
""" 
def gy_rm_substr(string_orig,sub_str):
    string_temp = string_orig
    while (sub_str in string_temp):
        string_temp = string_temp.replace(sub_str,"")
    else:
        return string_temp

print(gy_rm_substr(gy_string[0],'ab'))
print(gy_rm_substr(gy_string[1],'ab'))
   """  

"""
5.9看代码得结果（join用法）
x="abc",y="def",z=["d","e","f"],
分别求出x.join(y) 和x.join(z)返回的结果
"""
""" 
gy_x = "abc"
gy_y = "def"
gy_z = ["d","e","f"]

# new_str.join(orig_str) new_str as the connect string
print(gy_x.join(gy_y))
print(gy_x.join(gy_z))

 """

"""
5.10 看代码得结果（类和继承）
阅读以下代码，打印结果是什么？


"""
""" 
class A(object):

    def __init__(self):
        self.__Gender()
        self.Name()

    def __Gender(self):
        print("A.__Gender()")

    def Name(self):
        print("A.Name()")

class B(A):

    def __Gender(self):
        print("B.__Gender()")

    def Name(self):
        print("B.Name()")
b = B() """

"""

阅读以下代码，得到的结果是什么
https://blog.csdn.net/qdPython/article/details/107938206
"""
""" 
def fun():
    temp = [lambda x: i*x for i in range(4)]
    return temp

gy_list = range(0,4)
print(gy_list)
# temp = [lambda x : 0*x,lambda x : 1*x,lambda x : 2*x,lambda x : 3*x]

for everyLambda in fun(): 
    print(everyLambda(2))
 """

"""
5.12看代码得结果(列表推导式)

"""

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
#A0 = dict(('a',1),('b',2),('c',3),('d',4),('e',5))
#A0 = {'a':1,'b':2,'c':3,'d':4,'e':5}
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = [A0[s] for s in A0]
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]

print("A0:{}".format(A0)) #{'a':1,'b':2,'c':3,'d':4,'e':5}
print("A1:{}".format(A1)) #range(0,10)
print("A2:{}".format(A2)) #[]
print("A3:{}".format(A3)) #[1,2,3,4,5]
print("A4:{}".format(A4)) #[1,2,3,4,5]
print("A5:{}".format(A5)) #{0:0,1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81}
print("A6:{}".format(A6)) #[[0,0],[1,1],[2,4],[3,9],[4,16],[5,25],[6,36],[7,49],[8,64],[9,81]]