import threading
import time
from time import sleep 

class gy_thread(threading.Thread):

    def __init__(self,N,M):
        threading.Thread.__init__(self)
        self.paramter1 = N
        self.paramter2 = M

    def run(self):#define the thread function
        begin_time = time.time()
        for i in range(self.paramter1,self.paramter2,1):
            print("Enter run ",i)
            sleep(2)
        print("Spend time is ",time.time() - begin_time)

if __name__ == '__main__':
    gy_t1 = gy_thread(3,9)
    gy_t1.start()
    gy_t1.join()


        