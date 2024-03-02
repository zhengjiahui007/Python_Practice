import threading,time,os,datetime

'''
https://zhuanlan.zhihu.com/p/553207034
https://zhuanlan.zhihu.com/p/624943132?utm_id=0
产生死锁的方式：1.创建锁，没有解锁 ; 2.两个线程互相有对方的锁，然后互相等待


'''

class gy_thread(threading.Thread):
    def gy_doA(self):
        gy_lockR.acquire()
        print(self.name," got lockA ",datetime.datetime.now())
        time.sleep(3)
        gy_lockR.acquire()
        print(self.name," got lockB ",datetime.datetime.now())
        gy_lockR.release()
        gy_lockR.release()
        return

    def gy_doB(self):
        gy_lockR.acquire()
        print(self.name," got lockB ",datetime.datetime.now())
        time.sleep(3)
        gy_lockR.acquire()
        print(self.name," got lockA ",datetime.datetime.now())
        gy_lockR.release()
        gy_lockR.release()
        return

    def gy_doC(self):
        with gy_lockR:
            print(self.name," got gy_lockR ",datetime.datetime.now())
            self.gy_doB()
            time.sleep(2)
        return


    def run(self):
        #self.gy_doA()
        #self.gy_doB()
        self.gy_doC()
        return

class gy_threaddeadlock(threading.Thread):
    def gy_doA(self):
        gy_lockA.acquire()
        print(self.name," got lockA ",datetime.datetime.now())
        time.sleep(3)
        gy_lockB.acquire()
        print(self.name," got lockB ",datetime.datetime.now())
        gy_lockB.release()
        gy_lockA.release()
        return

    def gy_doB(self):
        gy_lockB.acquire()
        print(self.name," got lockB ",datetime.datetime.now())
        time.sleep(3)
        gy_lockA.acquire()
        print(self.name," got lockA ",datetime.datetime.now())
        gy_lockA.release()
        gy_lockB.release()
        return

    def run(self):
        self.gy_doA()
        self.gy_doB()
        return

if ("__main__" == __name__):
    gy_lockA = threading.Lock()
    gy_lockB = threading.Lock()
    gy_lockR = threading.RLock()
    gy_thread_list = []
    for i in range(0,5,1):
        gy_thread_list.append(gy_threaddeadlock())

    for gy_t in gy_thread_list:
        gy_t.start()

    for gy_t in gy_thread_list:
        gy_t.join()

