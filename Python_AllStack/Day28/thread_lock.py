import time,threading

'''
最后来总结一下，threading 模块中的5种锁

① 互斥锁：Lock，一次只能放行一个，可以通过 with 语句调用。

② 可重入锁：RLock，一次只能放行一个，可以通过 with 语句调用。

③ 条件锁：Condition，一次可以放行任意个，可以通过 with 语句调用。

④ 事件锁：Event，一次全部放行，不能通过 with 语句调用。

⑤ 信号量锁:semaphore，一次可以放行特定个，可以通过 with 语句调用。
'''

def gy_addnum():
    global num_gy
    #num_gy -= 1
    gy_lock.acquire()
    temp_num = num_gy
    time.sleep(0.1)
    num_gy = temp_num - 1
    gy_lock.release()


num_gy = 100

gy_tlist = []
gy_lock = threading.Lock()
for i in range(0,100,1):
    t = threading.Thread(target = gy_addnum,args = ())
    t.start()
    gy_tlist.append(t)

for t in gy_tlist:
    t.join()

print("The final num value is ",num_gy)
