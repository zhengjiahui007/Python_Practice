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
#Practice 2
my_list = [5,8,3,45,5]
one,two,three,four,five = my_list
print(one)
print(two)
print(three)
print(four)
print(five)
'''

'''
#Practice 3
import heapq
scores = [51,33,64,87,91,75,15,49,33,82]

print(heapq.nlargest(3,scores))
print(heapq.nsmallest(5,scores))
'''

my_list = [5,8,3,45,5]
print(my_list)
print(*my_list)

def sum_of_elements(*arg):
    total = 0
    for i in arg:
        total += i

    return total

result = sum_of_elements(*my_list)
print(result)

