import os,threading
import time


def gy_add_th(N):
    gy_sum = 0
    for i in range(1,N,1):
        gy_sum += i
    print("The sum is {}".format(gy_sum))
    print("T sum is %d" %gy_sum)
    print("Sum is ",gy_sum)
    return gy_sum


time_begin = time.time()


gy_add_th(1000000)
gy_add_th(1000000)


# t1_gy = threading.Thread(target = gy_add_th,args = (50000000,))
# t1_gy.start()

# t2_gy = threading.Thread(target = gy_add_th,args = (80000000,))
# t2_gy.start()

# t1_gy.join()
# t2_gy.join()

time_end = time.time()
print("The spent time is ",(time_end - time_begin))

gy_l = lambda x,y : x * y
print(gy_l(3,9))


