def func_damage(skill1,skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 9
    return damage1,damage2

damages = func_damage(4,9)
print(type(damages),damages,damages[0],damages[1])
#序列解包
skill1_damage,skill2_damage = func_damage(78,3)
print(skill1_damage,skill2_damage)