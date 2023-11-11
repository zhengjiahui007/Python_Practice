"""
实例001：数字组合
题目： 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
程序分析： 遍历全部可能，把有重复的剃掉
"""

total = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j) and (j != k) and (k != i):
                total1 = 100*i + j*10 + k;
                print("The number is %d%d%d,%d" %(i,j,k,total1))
                total += 1
                print('Total is %d' %(total))


'''
简便方法 用itertools中的permutations即可。
'''
import itertools
print("Use intertools!1")
sum = 0
sum_a = 0
iter_A = [1,2,3,4]
for i in itertools.permutations(iter_A,3):
    print(i)
    a,b,c = i
    print(a,b,c,sep='',end='\n')
    sum += 1
print("Total num is ",sum)