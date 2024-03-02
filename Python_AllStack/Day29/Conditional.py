import os,time,datetime,threading

'''
https://zhuanlan.zhihu.com/p/553393929
# 生成一个条件锁对象
cond = threading.Condition(Lock/Rlock),default is Rlock

# 上锁
cond.acquire()

# 解锁
cond.release()

# 挂起线程，直到收到一个 notify 通知才会被唤醒
cond.wait()

# 唤醒一个 Condition 的 waiting 池中的线程
cond.notify()

# 唤醒所有 Condition 的 waiting 池中的线程
cond.notify_all()
# Condition()对象中也实现了__enter__()与__exit__()魔法方法，所以也是可以通过 with 语句调用的
'''
class gy_producer_thread(threading.Thread):
    def __init__(self,name,cond):
        threading.Thread.__init__(self)
        self.condt = cond
        self.name = name
        return

    def run(self):
        global gy_counter
        while True:
            #print("2222",datetime.datetime.now())
            self.condt.acquire()
            gy_counter += 1
            if (gy_counter > 1):
                print(self.name," : gy_counter = ",gy_counter,datetime.datetime.now())
                self.condt.notify()
                self.condt.release()
                break
            print(self.name," : gy_counter = ",gy_counter,datetime.datetime.now())
            self.condt.notify()
            self.condt.release()
            time.sleep(1)
        return

class gy_consumer_thread(threading.Thread):
    def __init__(self,name,cond):
        threading.Thread.__init__(self,name = name)
        #self.name = name
        self.condt = cond
        return

    def run(self):
        global gy_counter
        while True:
            #print("1111",datetime.datetime.now())
            with self.condt:
                #self.condt.acquire()
                #print("333",datetime.datetime.now())
                self.condt.wait()
                #print("444",datetime.datetime.now())
                gy_counter -= 1
                if (0 != gy_counter):
                    print(self.name," : gy_counter = ",gy_counter,datetime.datetime.now())
                    break
                print(self.name," : gy_counter = ",gy_counter,datetime.datetime.now())
                #self.condt.release()
                #time.sleep(2)
        return

if ('__main__' == __name__):
    gy_counter = 0
    gy_condition_v = threading.Condition(threading.Lock())
    gy_thread_list = []
    gy_thread_list.append(gy_consumer_thread("gy_consumer_thread-0",gy_condition_v))
    for i in range(0,1,1):
        gy_thread_list.append(gy_producer_thread("gy_producer_thread-{}".format(i),gy_condition_v))


    for t in gy_thread_list:
        t.start()




