
"""
在一个内部函数里，对在外部作用域(但不是全局作用域)的变量进行引用，这个内部函数被认为是闭包

函数在定义时 + 其当时所在的环境变量 保存函数在定义时的一个环境/现场
"""
m_out = 100
def outer(z):
    x = 10
    y = 20
    print("out m_out = ",m_out)
    def inner(k):
        print(x + y + z + k)
        print("m_out = ",m_out)
    return inner

outer(32)(4)
f_in = outer(12)
f_in(6)
