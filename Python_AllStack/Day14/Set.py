gy_set = {'er','uop','yyt',1}
print(type(gy_set))
print(gy_set)
gy_set1 = {'yuiojh',9,0}

print(gy_set1)
gy_set2 = set('iopkj')
print(gy_set2)


#无序 不可重复 集合是非可哈希即可变 集合的元素需要可哈希
#frozenset
a = {1,5,6,8,9,4}
b = {4,5,9,80,7}

print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))
print(a.union(b))
print(a.symmetric_difference(b))

