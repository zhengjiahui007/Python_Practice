# Enum

#Enum,name of Enum,value of Enum
from enum import Enum

class GY_VIP(Enum):
    GY_YELLOW = 1
    GY_GREEN  = 2
    GY_BLACK  = 3
    GY_RED    = 4
""" 
gy_diamond = GY_VIP.GY_GREEN
print(gy_diamond == GY_VIP.GY_BLACK,type(GY_VIP))
print(GY_VIP.GY_BLACK.value,GY_VIP.GY_GREEN.name,GY_VIP.GY_RED)
print(type(GY_VIP.GY_BLACK.value),type(GY_VIP.GY_GREEN.name),type(GY_VIP.GY_RED))


class GY_Common():
    YELLOW_GY = 1

#GY_VIP.GY_GREEN = 9
GY_Common.YELLOW_GY = 8

for gy_e in GY_VIP:
    print(gy_e)

 """
""" 
print(GY_VIP.GY_RED == 5)
print(GY_VIP.GY_RED != GY_VIP.GY_YELLOW)

for gy_e in GY_VIP:
    print(gy_e)

for gy_e in GY_VIP.__members__.items():
    print(gy_e)

for gy_e in GY_VIP.__members__:
    print(gy_e)

 """

""" 
class GY_MVP(Enum):
    MVP_YELLOW = 1
    MVP_GREEN  = 'green'
    MVP_BLACK  = 3
    MVP_RED    = 4


print(GY_VIP.GY_GREEN == GY_MVP.MVP_GREEN)
print(type(GY_VIP.GY_GREEN))

gy_a = 2
print(GY_VIP(gy_a))
 """
from enum import IntEnum,unique

@unique
class GY_Colour(IntEnum):
    MVP_YELLOW = 1
    MVP_GREEN  = 2
    MVP_BLACK  = 3
    MVP_RED    = 4

# 单例模式






