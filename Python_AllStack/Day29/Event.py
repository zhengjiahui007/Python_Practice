import os,threading,time,datetime
'''
1.事件锁 Event
Event 是 python 中的事件锁，它是根据条件锁来实现的，条件锁一次可以放行任意个子线程，而事件锁一次只能放行全部。
Event 对象中有一个信号标志，默认为 False，可以把这个标志看做为一个红绿灯，绿灯通行红灯阻塞，如果一个线程等待一个 Event 对象，那么这个 Event 对象的标志将决定这个线程是否会被阻塞。需要注意的是，如果一个线程将 Event 对象的标志设置为真，那么所有等待这个 Event 对象的线程都将会被放行。
2.事件锁的使用

# 生成一个事件锁对象
eve = threading.Event()

# 将事件锁设置为红灯状态
eve.clear()
 
# 判断事件锁的状态
eve.is_set()

# 将当前线程设置’等待‘状态
eve.wait()

# 将事件锁设置为绿灯状态
eve.set()
'''

class gy_Boss_thread(threading.Thread):
    def __init__(self,name,event):
        threading.Thread.__init__(self)
        self.event = event
        self.name = name
        return

    def run(self):
        print(self.name,"Please OT tonight !",datetime.datetime.now())
        self.event.set()#notify all threads
        time.sleep(5)
        print(self.name,"Please got off work on 22:00 !",datetime.datetime.now())
        self.event.set()#notify all threads
        return

class gy_Worker_thread(threading.Thread):
    def __init__(self,name,event):
        threading.Thread.__init__(self,name = name)
        #self.name = name
        self.event = event
        return

    def run(self):
        self.event.wait()
        print(self.name,"Oh My God !",datetime.datetime.now())
        time.sleep(1)
        self.event.clear()
        self.event.wait()
        print(self.name,"Oh Yeah !",datetime.datetime.now())
        self.event.clear()
        return

if ('__main__' == __name__):
    gy_event = threading.Event()
    gy_thread_list = []
    for i in range(0,3,1):
        gy_thread_list.append(gy_Worker_thread("gy_Worker_thread-{}".format(i),gy_event))
    gy_thread_list.append(gy_Boss_thread("gy_Boss_thread-0",gy_event))
    for t in gy_thread_list:
        print(t.name)
        t.start()