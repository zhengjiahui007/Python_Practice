# -*- coding : utf-8 -*-
# __author__ : "Garry Zheng"
#!usr/bin/env python3

import os,sys,time
from  multiprocessing import Process,Queue,Pipe

'''
python-类的继承 构造方法的重写及继承
https://zhuanlan.zhihu.com/p/345723147
'''

def gy_process_que(que:Queue,proc_name:str):
    time.sleep(3)
    print("The name is ",proc_name)
    print("The ppid is ",os.getppid())
    print("The pid is ",os.getpid())
    que.put("123")
    print("sub proc : ",id(que))
    return


def gy_process_pipe(pip:Pipe,proc_name:str):
    time.sleep(3)
    print("The name is ",proc_name)
    print("The ppid is ",os.getppid())
    print("The pid is ",os.getpid())
    pip.send("Here is gy_process_pipe")
    print("sub proc : ",id(pip))
    return

def gy_process_pipe2(pip:Pipe,proc_name:str):
    time.sleep(3)
    print("The name 2 is ",proc_name)
    print("The ppid 2 is ",os.getppid())
    print("The pid 2 is ",os.getpid())
    pip.send("Here is gy_process_pipe2")
    print("sub proc : ",id(pip))
    return

def gy_proc_fun(proc_name:str):
    time.sleep(3)
    print("The name is ",proc_name)
    print("The ppid is ",os.getppid())
    print("The pid is ",os.getpid())
    return


class gy_process_class(Process):
    def __init__(self,name):
        #super(Process,self).__init__()
        super().__init__()##
        self.name = name
        return

    def run(self):
        time.sleep(3)
        print("The name is ",self.name)
        print("The ppid is ",os.getppid())
        print("The pid is ",os.getpid())
        return


if '__main__' == __name__:
    # gy_p = Process(target = gy_proc_fun,args = ("gy_proc_0",))
    # gy_p.start()
    # gy_p.join()

    # gy_proce_list = []
    # for i in range(0,3,1):
    #     gy_p = gy_process_class("gy_pro_%d"%(i))
    #     gy_proce_list.append(gy_p)
    #     gy_p.start()

    # for proc_i in gy_proce_list:
    #     proc_i.join()

    # gy_proce_list = []
    # gy_que = Queue()
    # print("main proc : ",id(gy_que))
    # gy_p = Process(target = gy_process_que,args = (gy_que,"gy_proc_0",))
    # gy_p.start()
    # print(gy_que.get())
    # gy_p.join()

    par_p,child_p = Pipe()
    print("main proc : ",id(par_p))
    gy_p = Process(target = gy_process_pipe,args = (child_p,"gy_proc_2",))
    gy_p1 = Process(target = gy_process_pipe2,args = (child_p,"gy_proc_21",))
    gy_p.start()
    gy_p1.start()
    print(par_p.recv())
    print(par_p.recv())
    gy_p.join()
    gy_p1.join()
