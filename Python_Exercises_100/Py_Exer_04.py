"""
实例004：这天第几天
题目： 输入某年某月某日，判断这一天是这一年的第几天？
程序分析： 特殊情况，闰年时需考虑二月多加一天：
"""

def isLeapyear(Year):
    if ((0 == Year%400) or ((0 == Year%4) and (100 != Year%100))):
        return True
    else:
        return False


def calulateTheDayNO(Y,M,D):
    DayNo = 0
    if ((0 > m_Year) or (0 > m_Month) or (12 < m_Month) or (0 > m_Day) or (31 < m_Day)):
        print("Please input the correct Date value !")
        return DayNo
    m_MonthDays_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    m_MonthDays_Leaplist = [31,29,31,30,31,30,31,31,30,31,30,31]
    DayNo = 0
    if (isLeapyear(Y)):
        for i in range(0,M - 1):
            DayNo += m_MonthDays_Leaplist[i]
        else:
            DayNo += D
    else:
        for i in range(0,M - 1):
            DayNo += m_MonthDays_list[i]
        else:
            DayNo += D
    return DayNo

m_Year = int(input("Please input the year : "))
m_Month = int(input("Please input the month : "))
m_Day = int(input("Please input the day : "))


m_NODay = calulateTheDayNO(m_Year,m_Month,m_Day)
if (0 != m_NODay):
    print("The %d.%d.%d" %(m_Year,m_Month,m_Day)," is the NO.%d in the year!" %(m_NODay))


DofM = [0,31,28,31,30,31,30,31,31,30,31,30]
res=0
year=int(input('Year:'))
month=int(input('Month:'))
day=int(input('day:'))
if isLeapyear(year):    
  DofM[2]+=1
for i in range(month):    
  res+=DofM[i]
print(res+day)