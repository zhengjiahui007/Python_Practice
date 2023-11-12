"""
实例009：暂停一秒输出
"""
""" 
import time
for i in range(0,4,1):
    print(str(int(time.time())))
    print(str(int(time.time()))[-2:])
    time.sleep(1)
 """

"""
实例010：给人看的时间
题目： 暂停一秒输出，并格式化当前时间。
程序分析： 使用 time 模块的 sleep() 函数。
"""

""" 
for i in range(0,4,1):
  print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
  time.sleep(1)
"""

""" 
实例016：输出日期
题目: 输出指定格式的日期。
程序分析: 使用 datetime 模块。
"""

import datetime

print(datetime.date.today())
print("Today is ",datetime.date(2023,11,12))
print("Today is ",datetime.date.today().strftime("%d/%m/%Y"))
m_day = datetime.date(1111,2,3)
print("m_day is ",m_day)
m_day = m_day.replace(year=m_day.year + 22)
print("m_day is ",m_day)




