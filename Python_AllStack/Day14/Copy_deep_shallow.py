# gy_list_0 = [1,3,2,'garry','zheng']

# gy_list_1 = gy_list_0.copy()
# print(gy_list_0)
# print(gy_list_1)

# gy_list_1[1] = 9

# print(gy_list_0)
# print(gy_list_1)

#Shallow Copy,copy the first level
# gy_list_0 = [1,[16,78,5],2,'garry','zheng']

# gy_list_1 = gy_list_0.copy()
# print(gy_list_0)
# print(gy_list_1)

# gy_list_1[1][2] = 9

# print(gy_list_0)
# print(gy_list_1)

# tuple can not be modified
# gy_tuple = (1,3,4,2,6)
# gy_tuple[2] = 99
# print(gy_tuple)

# gy_husband = ['Garry',12345,[15000,9000]]
# gy_wife = gy_husband.copy()

# gy_wife[0] = 'XY'
# gy_wife[1] = 33453

# gy_husband[2][1] -= 2000

# print(gy_husband,gy_wife)

# import copy

# gy_list_0 = [1,[16,78,5],2,'garry','zheng']

# gy_list_1 = copy.deepcopy(gy_list_0)
# print(gy_list_0)
# print(gy_list_1)

# gy_list_1[1][2] = 9

# print(gy_list_0)
# print(gy_list_1)

gy_x = [1,2,3,4]

gy_y = gy_x 
print(gy_x,id(gy_x),id(gy_x[0]),id(gy_x[1]),id(gy_x[2]),id(gy_x[3]))
print(gy_y,id(gy_y),id(gy_y[0]),id(gy_y[1]),id(gy_y[2]),id(gy_y[3]))

gy_y[2] = 8
print(gy_x,id(gy_x),id(gy_x[0]),id(gy_x[1]),id(gy_x[2]),id(gy_x[3]))
print(gy_y,id(gy_y),id(gy_y[0]),id(gy_y[1]),id(gy_y[2]),id(gy_y[3]))

gy_y = [2,3,1,0]

print(gy_x,id(gy_x),id(gy_x[0]),id(gy_x[1]),id(gy_x[2]),id(gy_x[3]))
print(gy_y,id(gy_y),id(gy_y[0]),id(gy_y[1]),id(gy_y[2]),id(gy_y[3]))
