class Harman_gz():
    def __init__(self) -> None:
        return None

    @property
    def har_propprint(self):
        print("This is property !")
        return 4

    @har_propprint.setter
    def har_setpprint(self,a:int):
        print("This is har_setpprint a = ",a)
        return None

    @har_propprint.deleter
    def har_delpprint(self):
        print("This is har_delpprint !")
        return None

########################Another style #####################
    def harman_propprint(self):
        print("This is harman_propprint !")
        return 40

    def harman_setpprint(self,a:int):
        print("This is harman_setpprint a = ",a)
        return None

    def harman_delpprint(self):
        print("This is harman_delpprint !")
        return None

    harman_pro = property(harman_propprint,harman_setpprint,harman_delpprint)


obj_gz = Harman_gz()
print(obj_gz.har_propprint)

obj_gz.har_setpprint = 3

del obj_gz.har_delpprint

print(obj_gz.harman_pro)

obj_gz.harman_pro = 89

del obj_gz.harman_pro

'''
[表达式 for 变量 in 列表] 
[out_exp_res for out_exp in input_list]

或者 

[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]
'''
""" 
k_list = list(range(0,10,1))
print(f"k_list is {k_list}")


k_list1 = [k for k in range(0,10,1)]
print("k_list1 is {}".format(k_list1))

k_list2 = []
for i in range(1,11,1):
    k_list2.append(i)
print("k_list2 is {}".format(k_list2))
 """
class page_list():
    page_total_list = list(range(1,1001,1))
    def __init__(self,curpage_index) -> None:
        try:
          page_index = int(curpage_index)
        except Exception as e:
          print('An exception occurred')
          page_index = 1
        self.currentpage = page_index
        print("currentpage = ",self.currentpage)
        return None

    @property
    def page_start(self):
        start = (self.currentpage - 1)
        return start

    @property
    def page_end(self):
        end = self.currentpage + 9
        return end

########################Another style #####################
    def start_page(self):
        start = (self.currentpage - 1)
        return start

    def end_page(self):
        end = self.currentpage + 9
        return end

    page_startpro = property(start_page)
    page_endpro = property(end_page)

""" 
while True:
    p_start = input("Please input a page number : ")
    obj_page = page_list(p_start)
    print(page_list.page_total_list[obj_page.page_start:obj_page.page_end:1])
    break
"""
""" 
while True:
    p_start = input("Please input a page number : ")
    obj_page = page_list(p_start)
    print(page_list.page_total_list[obj_page.page_startpro:obj_page.page_endpro:1])
    break

 """