""" 
m_Name = "Garry"
m_Years = 38
print("{} is {}".format(m_Name,m_Years))

实例007：copy
题目： 将一个列表的数据复制到另一个列表中。
程序分析： 使用列表[:]，拿不准可以调用copy模块。
"""
"""
shallow copy :
浅拷贝只是拷贝表层的内容。拷贝会生成一个新的对象，新生成对象的id与原对象的id不同，
由于浅拷贝只会拷贝最表层的对象，因此当被拷贝对象中存在子对象时，
子对象的id不会发生改变，会与原对象中子对象的id保持一致。

浅拷贝仅拷贝对象本身的内容并创建新对象，
但是，对象中的对象即子对象仍然只是复制了地址而不是新创建同内容的子对象

常见的浅拷贝方法
1. 切片
2. 利用工厂函数（可变对象的工厂函数，list、dict、set）
3. 利用对象自带的copy方法啊（只有可变类型的数据类型有该方法，如list、dict、set）
4. 利用copy库中的copy方法

ndarray
  切片：浅拷贝。
  numpy.copy()：深拷贝

Python 使用引用来管理内存和处理对象。变量和对象有各自的存储空间，两者相互独立。变量存储对象的内存地址，
即把对象的地址写入变量，即创建了一个引用。变量和对象创建引用后，可以通过变量名来访问对象的属性和方法

每个对象除了这三个基本属性以外，在使用过程中，用户经常会通过加标签的方式给对象附加一个标识符，也称为名字（name），
以方便在程序中通过这个名字引用该对象。这个名字与其他程序设计语言中的变量作用相似，
所以 Python 中也经常称之为变量。Python中用赋值符号（=）给对象加标识符，
也可以说是给对象增加名字或是没用传统称为给变量赋值。同一个对象可以命多个名字，不同对象命相同名字时，应用时访问最邻近命名的那个对象。
https://blog.51cto.com/u_16213715/7788939


https://blog.csdn.net/iamballer77/article/details/127722933

https://www.baidu.com/link?url=8nYIDSEuiBTTTkLP01Bxxyi2GiFNBddRJmlsJsxYIFh44CNugvzS90-TvqXT_8HDgmSnFAWGcT_GNXaPumm2NsshfreNb1V1k-qH1SObwMa&wd=&eqid=9ee715be000666ef000000066550a762
"""

import copy
m_gy_list = [1,2,3,"qw",[5,7]]

print(id(m_gy_list[0]),id(1))

""" 
m_gy_a = m_gy_list #赋值,m_gy_a/m_gy_list 指向同一个list对象 [1,2,3,"qw",[5,7]]
m_gy_b = m_gy_list[::1] #浅copy
m_gy_c = copy.copy(m_gy_list) #浅copy
m_gy_d = copy.deepcopy(m_gy_list) #深copy

m_gy_list.append(8)
m_gy_list[4].append(80)
"""

""" 
print("m_gy_list = ",m_gy_list,id(m_gy_list),id(m_gy_list[0]),id(m_gy_list[1]),id(m_gy_list[2]),id(m_gy_list[3]),id(m_gy_list[4]),id(m_gy_list[4][0]),id(m_gy_list[4][1]))
print("m_gy_a = ",m_gy_a,id(m_gy_a),id(m_gy_a[0]),id(m_gy_a[1]),id(m_gy_a[2]),id(m_gy_a[3]),id(m_gy_a[4]),id(m_gy_a[4][0]),id(m_gy_a[4][1]))
print("m_gy_b = ",m_gy_b,id(m_gy_b),id(m_gy_b[0]),id(m_gy_b[1]),id(m_gy_b[2]),id(m_gy_b[3]),id(m_gy_b[4]),id(m_gy_b[4][0]),id(m_gy_b[4][1]))
print("m_gy_c = ",m_gy_c,id(m_gy_c),id(m_gy_c[0]),id(m_gy_c[1]),id(m_gy_c[2]),id(m_gy_c[3]),id(m_gy_c[4]),id(m_gy_c[4][0]),id(m_gy_c[4][1]))
print("m_gy_d = ",m_gy_d,id(m_gy_d),id(m_gy_d[0]),id(m_gy_d[1]),id(m_gy_d[2]),id(m_gy_d[3]),id(m_gy_d[4]),id(m_gy_d[4][0]),id(m_gy_d[4][1]))
"""