import time,threading

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
