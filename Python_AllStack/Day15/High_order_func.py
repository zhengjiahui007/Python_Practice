
# High order / level function

# function as a paramter of a function

def gy_func(**kwargs):
    print(kwargs)


gy_func(**{'age':15,'name':'Garry'})

# function as a return value