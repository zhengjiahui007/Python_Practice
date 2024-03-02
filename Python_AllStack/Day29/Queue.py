'''
二、Queue

Queue 的内部使用 deque() 实现，deque() 是 python 中的双端队列，它是线程安全的，所以多个线程在使用的时候不会造成数据污染。

1.Queue 的使用

# 生成一个 Queue 对象，maxsize 默认为 0
queue = Queue(maxsize=1000)

# 写入数据，如果队列已满，会一直阻塞
queue.put()

# 相当于queue.put(block=False) 
queue.put_nowait()  

# 获取数据，如果队列为空，会一直阻塞
queue.get()  

# 相当于queue.get(block=False)  
queue.get_nowait()

# 等待队列被消费完，从 queue 的角度阻塞主线程
queue.join()

# 通知队列任务处理完成，join 阻塞将会解除
queue.task_done()

# 获取队列长度
queue.qsize()  
 
# 判断队列是否为空
queue.empty()

# 判断队列是否已满
queue.full()   



import threading
import queue
import time


def producer(que):
    print('producer producing goods start')
    for i in range(1, 6):
        que.put(f'good_{i}')
    print('producer producing goods end')

def consumer(que):
    goods_name = que.get()
    print(f'consumer consuming goods: {goods_name} start')
    time.sleep(1)
    print(f'consumer consuming goods: {goods_name} end')
    if que.empty():
        que.task_done()   # 通知队列任务处理完成



if __name__ == '__main__':
    que = queue.Queue(maxsize=100)
    pro_thread = threading.Thread(target=producer, args=(que,))
    pro_thread.start()

    time.sleep(1)   # sleep 1s 确保生产者先将数据写入队列
    while not que.empty():
        con_thread = threading.Thread(target=consumer, args=(que,))
        con_thread.start()
        
    print(que.empty())
    que.join()   # 等待队列被消费完再执行下面的流程
    print('---end---')
'''

import os,time,datetime,threading
import queue
from random import randint


# gy_Que = queue.Queue(3)

# gy_Que.put("Garry")
# gy_Que.put("VS")
# gy_Que.put(2)
# gy_Que.put(4,block = False,timeout = 3)

# #FIFO
# print(gy_Que.get())
# print(gy_Que.get())
# print(gy_Que.get())
# print(gy_Que.get())

class gy_producer_thread(threading.Thread):
    def __init__(self,name,que):
        threading.Thread.__init__(self)
        self.queue = que
        self.name = name
        return

    def run(self):
        while True:
            gy_counter = randint(0,100)
            gy_que.put(gy_counter)
            print(self.name,"put : gy_counter = ",gy_counter)
            time.sleep(1)
        return

class gy_consumer_thread(threading.Thread):
    def __init__(self,name,que):
        threading.Thread.__init__(self,name = name)
        #self.name = name
        self.queue = que
        return

    def run(self):
        while True:
            gy_counter = gy_que.get()
            print(self.name,"get : gy_counter = ",gy_counter)
            if gy_que.empty():
                print(" ****************** ")
        return

if ('__main__' == __name__):
    gy_que = queue.Queue(10)
    gy_thread_list = []
    
    for i in range(0,4,1):
        gy_thread_list.append(gy_producer_thread("gy_producer_thread-{}".format(i),gy_que))
    gy_thread_list.append(gy_consumer_thread("gy_consumer_thread-0",gy_que))
    for t in gy_thread_list:
        t.start()