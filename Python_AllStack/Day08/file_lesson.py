
import time
# gy_file = open('小重山','r',encoding = 'utf-8')

# file_connent = gy_file.read(6) #中文也是一个size是一个字符
# print(file_connent)

# file_connent = gy_file.read(6) # file handle will move with the read size

# gy_file.write('Garry Zheng\n')
# gy_file.write('Alexa Zheng')

# file_connent = gy_file.readline()
# print(file_connent)

# file_connent1 = gy_file.readline()
# print(file_connent1)

# file_connent1 = gy_file.readlines()
# gy_file.close()
# print(file_connent1)

# # new_str_gy = file_connent1[5].strip() + "I like it!" 
# # print(new_str_gy)

# print(''.join((file_connent1[5].strip(),'I love it')))

# for i_file in range(0,len(file_connent1),1):
#     if 5 == i_file:
#         print(file_connent1[i_file].strip() + "I like it!")
#     else:
#         print(file_connent1[i_file].strip())


# for i_file in range(0,len(file_connent1),1):
#     if 5 == i_file:
#         print(''.join([file_connent1[i_file].strip(),"I like it!"]))
#     else:
#         print(file_connent1[i_file].strip())

# i_file_index = 0
# for i_file in file_connent1:
#     i_file_print = i_file.strip()
#     if 5 == i_file_index:
#         i_file_print = ''.join([i_file.strip(),"I choose it!"])
#     print(i_file_print)
#     i_file_index += 1


# gy_file = open('小重山','r',encoding = 'utf-8')

#迭代器
# for i_file in gy_file:
#     #print(type(i_file))
#     print(i_file.strip())


# print(gy_file.tell())
# print(gy_file.read(4))
# print(gy_file.tell())
# print(gy_file.read(5))
# gy_file.seek(0)
# print(gy_file.tell())
# print(gy_file.read(5))
# gy_file.close()

# flush method

import sys,time

# for i in range(0,50,1):
#     sys.stdout.write('*')
#     sys.stdout.flush()
#     time.sleep(1)

# for i in range(0,50,1):
#     print('*',end = '',flush = True)
#     time.sleep(0.1)

#truncate（）：截断数据(不能在r模式下)
#在w模式下：先清空，再写，再截断
#在a模式下：直接将指定位置后的内容截断
# gy_file = open('小重山_1','a',encoding = 'utf-8')

# #gy_file.truncate(2)
# #print(gy_file.isatty())# whether tty machine mode
# gy_file.close()

# gy_file = open('小重山_1','r+',encoding = 'utf-8') #write from the original end,tag locate at the begginning

# file_connent1 = gy_file.readline()
# print(file_connent1)
# gy_file.write('95533')
# gy_file.close()

# gy_file = open('小重山_1','w+',encoding = 'utf-8') # clean if file has content

# #file_connent1 = gy_file.readline()
# #print(file_connent1)
# gy_file.write('95533')
# gy_file.seek(0)
# print(gy_file.readline())
# gy_file.close()


# gy_file = open('小重山_1','a+',encoding = 'utf-8') # open and the tag locates at last

# #file_connent1 = gy_file.readline()
# #print(file_connent1)
# # gy_file.write('95533')
# # gy_file.seek(0)
# print(gy_file.readline())
# gy_file.write('1234')
# print(gy_file.readline())
# gy_file.close()

# Final question

# import os

# gy_file = open('小重山','r+',encoding = 'utf-8')
# gy_file_1 = open('小重山_2','w+',encoding = 'utf-8')

# line_idex = 0
# for i_line in gy_file:
#     line_idex += 1
#     if (6 == line_idex):
#         gy_file_1.write(''.join([i_line.strip(),'Garry','\n']))
#     else:
#         gy_file_1.write(i_line)

# gy_file.close()
# gy_file_1.close()

# os.remove('小重山')
# os.remove('小重山_1')
# os.rename('小重山_2','小重山')

# open several file objects, will close when exit 'with' process
with open('小重山','r+',encoding = 'utf-8') as gy_file:
    for i_line in gy_file:
        print(i_line,end = "")














