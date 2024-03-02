import os,threading,datetime,time



class gy_thread(threading.Thread):
    Semph_Th = threading.Semaphore(6)
    Semph_ThB = threading.BoundedSemaphore(2)
    def __init__(self,semp):
        threading.Thread.__init__(self)
        self.semph = threading.Semaphore(6)
        return

    def run(self):
        #self.semph.acquire()
        #gy_thread.Semph_Th.acquire()
        gy_thread.Semph_ThB.acquire()
        print(self.name," : ",datetime.datetime.now())
        time.sleep(2)
        #self.semph.release()
        #gy_thread.Semph_Th.release()
        gy_thread.Semph_ThB.release()
        return


if ('__main__' == __name__):
    gy_sem = threading.Semaphore(6)
    gy_th_list = []
    for i in range(0,10,1):
        gy_th_list.append(gy_thread(gy_sem))
    for t in gy_th_list:
        t.start()