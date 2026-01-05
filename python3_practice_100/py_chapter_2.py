"""
2.1.水仙花数
如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
那么问题来了，求1000以内的水仙花数（3位数）
"""
""" 
for n in range(100,1000):
    n_str = str(n)
    n_0 = int(n_str[0])
    n_1 = int(n_str[1])
    n_2 = int(n_str[2])
    if (n == n_0**3 + n_1**3 + n_2**3):
        print(n,end = " ")
 """

"""
2.2完全数
如果一个正整数等于除它本身之外其他所有除数之和，就称之为完全数。
例如：6是完全数，因为6 = 1+2+3；
下一个完全数是28 = 14+7+4+2+1。
求1000以下的完全数
"""
""" 
for gy_n in range(1,1001,1):
    sum_i = 0
    for i in range(1,gy_n,1):
        if (0 == gy_n%i):
            sum_i += i
    if (gy_n == sum_i):
        print(gy_n,end = " ")

 """
"""
2.3 数字1-100求和
求1+2+3…+100和
"""

""" 
gy_sum = 0
for gy_n in range(1,101,1):
    gy_sum += gy_n

print("Ths sum of 1 - 100 is %d ."%gy_sum)

 """

"""
2.4计算求1-2+3-4+5-…-100的值
计算求1-2+3-4+5-…-100的值
"""
""" 
gy_sum = 0
for gy_n in range(1,101,1):
    if (0 == gy_n%2):
        gy_sum -= gy_n
    else:
        gy_sum += gy_n
print(gy_sum)
 """

"""
2.5计算求1+2-3+4-5... ...100 的值
计算求1+2-3+4-5... ...100 的值
"""
""" 
gy_sum = 1
for gy_n in range(2,101,1):
    if (0 == gy_n%2):
        gy_sum += gy_n
    else:
        gy_sum -= gy_n
print(gy_sum)
 """

"""
2.6计算 1-n 之间的所有 5 的倍数之和
定义一个函数：计算 1-n 之间的所有 5 的倍数之和，默认计算 1-100 （ n 是 一个整数）
"""
""" 
gy_N = int(input("Please input an integer :"))
sum_5 = 0
for gy_n in range(1,gy_N + 1,1):
    if (0 == gy_n%5):
        sum_5 += gy_n
print(sum_5)

sum_5 = 0
for gy_n in range(1,20,1):
        sum_5 += gy_n*5
print(sum_5)

 """

"""
2.7 n个自然数的立方和
计算公式 13 + 23 + 33 + 43 + …….+ n3
实现要求：
输入 : n = 5
输出 : 225
对应的公式 : 13 + 23 + 33 + 43 + 53 = 225
"""
""" 
gy_N = int(input("Please input an integer :"))

gy_sum_nnn = 0
for gy_n in range(1,gy_N + 1,1):
    gy_sum_nnn += gy_n ** 3
print(gy_sum_nnn)
 """

"""
2.8 阶乘10!
阶乘的意思: 10!=10x9x8x7x6x5x4x3x2x1
求10!
"""
""" 
gy_N = int(input("Please input an integer :"))

gy_factorial = 1
for gy_n in range(1,gy_N + 1,1):
    gy_factorial *= gy_n
print(gy_factorial)
 """

"""
2.9求1+2!+3!+...+10!的和
求1+2!+3!+...+10!的和
"""
""" 
gy_N = int(input("Please input an integer :"))
gy_sum_n_factorial = 0

for gy_n in range(1,gy_N + 1,1):
    gy_factorial = 1
    for gy_m in range(1,gy_n + 1,1):
        gy_factorial *= gy_m
    gy_sum_n_factorial += gy_factorial
print(gy_sum_n_factorial)
 """

"""
2.10求s=a+aa+aaa+aaaa+aa...a的值
求s=a+aa+aaa+aaaa+aa...a的值

如：n = 5  a = 3
33333 = 3x10**4+ 3x10**3+ 3x10**2 + 3x10**1 +3x10**0
"""
""" 
gy_N = int(input("Please input an integer for N:"))
gy_A = int(input("Please input an integer for A:"))

gy_sum_N = 0
gy_AAA = 0

for gy_n in range(0,gy_N,1):
    gy_AAA = 0
    for gy_m in range(0,gy_n + 1,1):
        gy_AAA += gy_A * 10 ** gy_m
    gy_sum_N += gy_AAA
    print("gy_AAA = %d "%gy_AAA)
print(gy_sum_N)
 """

"""
2.11 斐波那契数列1、1、2、3、5、8、13 .....
已知一个数列：1、1、2、3、5、8、13、。。。。的规律为从 3 开始的每一项都等于其前两项的和，这是斐波那契数列。
求满足规律的 100 以内的所有数据
"""

gy_N = int(input("Please input an integer for N:"))
gy_list_Fibonacci = [1,1]
""" 
gy_fibonacci = 1 + 1
gy_fibonacci_pre_0 = 1
gy_fibonacci_pre_1 = 1
gy_fibonacci_next = gy_fibonacci_pre_0 + gy_fibonacci_pre_1
gy_list_Fibonacci.append(gy_fibonacci_next)
while gy_N >= gy_fibonacci_next:
    gy_fibonacci_pre_0 = gy_fibonacci_pre_1
    gy_fibonacci_pre_1 = gy_fibonacci_next
    gy_fibonacci_next = gy_fibonacci_pre_0 + gy_fibonacci_pre_1
    if gy_N < gy_fibonacci_next:
        break
    gy_list_Fibonacci.append(gy_fibonacci_next)
 """

gy_fibonacci_next = gy_list_Fibonacci[-2] + gy_list_Fibonacci[-1]
while gy_N >= gy_fibonacci_next:
    gy_fibonacci_next = gy_list_Fibonacci[-2] + gy_list_Fibonacci[-1]
    if gy_N < gy_fibonacci_next:
        break
    gy_list_Fibonacci.append(gy_fibonacci_next)

print(gy_list_Fibonacci)













    









