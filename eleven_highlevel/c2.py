#函数式编程

#闭包：函数在定义时 + 其当时所在的环境变量 保存函数在定义时的一个环境/现场
# 一切皆对象
""" 
def curve_pre(gg_a):
    gy_a = 3
    def curve(gy_x):
        return gy_a*gy_x*gy_x
    return curve

gy_a = 9
gy_f = curve_pre(3)
print(gy_f.__closure__)
print(gy_f.__closure__[0].cell_contents)
print(gy_f(3))
 """
""" 
def gy_f1():
    gy_a = 10
    def gy_f2():
        # gy_a 是局部变量，没有引用外部的环境变量gy_a,所以不存在闭包
        #gy_a = 12
        gy_c = gy_a * 3
        #return gy_a
    return gy_f2

gy_func = gy_f1()
print(gy_func)
print(gy_func.__closure__)


 """

gy_origin = 0

""" 
def gy_go(gy_s):
    global gy_origin
    new_pos = gy_origin + gy_s
    gy_origin = new_pos #认为gy_origin是局部变量，因为有赋值
    return new_pos
 """

gy_origin = 0

def gy_go(gy_position):
    def gy_go_1(gy_step):
        nonlocal gy_position
        new_pos = gy_position + gy_step
        gy_position = new_pos
        return gy_position
    return gy_go_1

gy_fu = gy_go(gy_origin)

print(gy_fu(2))
print(gy_fu.__closure__)
print(gy_fu.__closure__[0].cell_contents)
print(gy_fu(3))
print(gy_fu(26))
print(gy_origin)































