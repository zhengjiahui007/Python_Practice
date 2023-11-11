"""
实例002：“个税计算”
题目： 企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？
程序分析： 分区间计算即可。
"""

profit_rmb = int(input("Please input the profit (unit:RMB yuan): "))
bonus = 0
if profit_rmb <= 100000:
    bonus = profit_rmb * 0.1
elif (profit_rmb > 100000) and (profit_rmb < 200000):
    bonus = 100000 * 0.1 + (profit_rmb - 100000) * 0.075
elif (profit_rmb >= 200000) and (profit_rmb < 400000):
    bonus = 100000 * 0.1 + 100000 * 0.075 + (profit_rmb - 200000) * 0.05
elif (profit_rmb >= 400000) and (profit_rmb < 600000):
    bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + (profit_rmb - 400000) * 0.03
elif (profit_rmb >= 600000) and (profit_rmb < 1000000):
    bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + (profit_rmb - 600000) * 0.015
elif (profit_rmb >= 1000000):
    bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015 + (profit_rmb - 1000000) * 0.01

print("My bonus is ",bonus)


print("The other method is : ")


profit_list = [100000,200000,400000,600000,1000000]
profit_rate = [0.1,0.075,0.05,0.03,0.015,0.01]
thresholds = [100000,100000,200000,200000,400000]


bonus = 0
i = 0
j = 0
for i in range(0,len(profit_list),1):
    if (profit_rmb < profit_list[i]):
        print("1 The list id is ",i)
        if 0 != i:
            for j in range(0,i):
                bonus += (thresholds[j] * profit_rate[j])
            profit_rmb -= profit_list[j]
            bonus += profit_rmb * profit_rate[i]
            print("1 The bonus is ",bonus)
            break
        else:
            bonus += profit_rmb * profit_rate[i]
            print("3 The bonus is ",bonus)
            break

else:
    print("2 The list id is ",i)
    for j in range(0,i + 1):
        bonus += (thresholds[j] * profit_rate[j])
    profit_rmb -= profit_list[j]
    bonus += profit_rmb * profit_rate[-1]
    print("2 The bonus is ",bonus)
