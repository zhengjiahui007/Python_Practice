#参数

""" 
1.必须参数
2.关键字参数 
3.默认参数

"""
# add two value
""" def func_add(x,y):
    return (x + y)

c = func_add(y = 9,x = 8)

print(c) """

def func_print_studentinfo(name,gender = 'Boy',age = 8,school = "Harman"):
    print("My name is " + str(name) + " !")
    print("I am a " + str(gender) + " !")
    print("I am " + str(age) + " years old !")
    print("I am studying at " + str(school) + " !")
    return

func_print_studentinfo("Garry","Boy",9,"Harman")
print("**************************************")
func_print_studentinfo('Chili')
print("**************************************")
func_print_studentinfo('Bill',age = 9)