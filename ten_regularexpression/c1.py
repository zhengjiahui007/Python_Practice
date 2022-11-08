'''
Regular expression:

a special string list
一个字符串是否与我们所设定的
这样的字符序列，相匹配

快速检索文本，实现一些替换文本

普通字符

元字符


'''


import re
""" 
gy_a = 'C9C007Python4Java'

gy_r = re.findall('\d',gy_a)
print(gy_r)

gy_ch = re.findall('\D',gy_a)
print(gy_ch)

 """

#字符集
# gy_s = 'abc,acc,adc,aec,afc,abc'
# gy_r_ch = re.findall('a[cf]c',gy_s)
# print(gy_r_ch)


#概括字符集
# \d,\D,
# \w [A-Za-z0-9_] 单词字符
# \W 非单词字符
# \s 空白字符 ; \S 非空白字符
""" 
gy_a = 'C9C007Pyt@#&hon4*() Jav\na'
gy_r = re.findall('\w',gy_a)
print(gy_r)

gy_r = re.findall('[A-Za-z0-9_]',gy_a)
print(gy_r)

gy_r = re.findall('\W',gy_a)
print(gy_r)

 """

"""
数量词：贪婪与非贪婪


"""

'''
gy_a = 'C9C007Python@#&hon4*() Java\naPHP89df'
gy_r = re.findall('[a-zA-Z]{3,6}?',gy_a)
print(gy_r)

gy_r = re.findall('[a-zA-Z]{3,6}',gy_a)
print(gy_r)
'''

# * match the char before  * 0 or infinite times
# + match the char before  + 1 or infinite times
# ? match the char before  ? once or 0
""" 
gy_a = 'pytho0python1pythonn2'

print(re.findall('python*',gy_a))

print(re.findall('python+',gy_a))

print(re.findall('python?',gy_a))

print(re.findall('python{0,2}?',gy_a))
 """

# 边界匹配 ^  $
""" 
gy_QQ = '330431976'
print(re.findall('^\d{4,8}$',gy_QQ))

gy_QQ = '100000001'
print(re.findall('^000',gy_QQ))
 """
#Group
# [] is or, () is and
""" 
gy_a = 'PythonPythonPythonPythonPython'
print(re.findall('(Python){3}',gy_a))
print(re.findall('PythonPythonPython',gy_a))

 """

# flag paramter
""" 
gy_l = 'PythonC#\nJavaPHP'
print(re.findall('c#.{1}',gy_l,re.I | re.S))
 """


"""
正则替换
"""

gy_lan = 'PythonC#JavaPC#HC#P'

# print(re.sub('C#','GO',gy_lan,0))
# print(re.sub('C#','GO',gy_lan,1))
# print(re.sub('C#','GO',gy_lan,2))
# print(re.sub('C#','GO',gy_lan,4))

""" 
def gy_covert(value_gy):
    gy_mat = value_gy.group()
    return '!!' + gy_mat + '!9'

print(re.sub('C#',gy_covert,gy_lan,0))
 """
""" 
gy_s = 'AH35JDU34F6JCV4JDSK8J'

def gy_convert(val_gy):
    matched = val_gy.group()
    print(matched,end = " ")
    if (50 <= int(matched)):
        return '9'
    else:
        return '0'

print(re.sub('\d{2}',gy_convert,gy_s,0))
 """

""" 
gy_s = '35JDU34F6JCV4JDSK8J'
gy_r1 = re.match('\d',gy_s)
print(gy_r1.span())
gy_r2 = re.search('\d',gy_s)
print(gy_r2.group())
gy_r3 = re.findall('\d',gy_s)
print(gy_r3)

 """

#Group method
gy_s = 'Life is short,I use Python!'
gy_r = re.search('Life(.*)Python',gy_s)

print(gy_r.group(0))
print(gy_r.group(1))
#print(gy_r.group(3))
print(gy_r.groups())
gy_r = re.findall('(e)(.*)(Py)',gy_s)

print(gy_r)

gy_r = re.findall('e(.*)Py',gy_s)

print(gy_r)





