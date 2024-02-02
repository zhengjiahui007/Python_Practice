import os,time, threading
from time import ctime,sleep

def gy_music(func):
    for i in range(0,2,1):
        print("I am listening the %s . %s" %(func,ctime()))
        sleep(4)
        print("listen end time ",ctime())

def gy_movie(func):
    for i in range(0,2,1):
        print("I am watching the %s . %s " %(func,ctime()))
        sleep(5)
        print("watch end time ",ctime())


if __name__ == "__main__":
    begin_time = time.time()
    # gy_music(u"My heart will go on")
    # gy_movie(u"Face off")
    gy_thread_list = []
    gy_th1 = threading.Thread(target = gy_music,args = (u"My heart will go on",))
    gy_th2 = threading.Thread(target = gy_movie,args = (u"Face off",))
    gy_thread_list.append(gy_th1)
    gy_thread_list.append(gy_th2)
    gy_th2.daemon = True
    for t in gy_thread_list:
        #t.setDaemon(True)
        t.start()
    #t.join()
    print("The total timme is ",(time.time() - begin_time))





