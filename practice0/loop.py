from readline import write_history_file


counter = 0
while counter < 10:
    counter += 1
    print(counter)
else:
    print("I am here")

a = [(1,3,5),["apple","baa","org","lemon"]]
for x in a:
    for y in x:
        if y == 5:
            break;
        print(y)
else:
    print("I am not here")

    
while