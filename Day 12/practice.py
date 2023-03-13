#scope
num = 1                                 #global scope
num2 = 3
PI = 3.14                               #global constant, can't be changed
def increase_num():                     #local scope
    num = 2                             #will affect inside the function
    print(f"Inside function: {num}")
    print(f"Inside function: {num2}")
def modify():
    global num
    num += 1
def modify2():
    num = 4
    num += 1
    return num
increase_num()                          #won't affect outside the function
print(f"Outside function: {num}")
print(f"Outside function:{num2}")
modify()                                #modifies the global variable
print(f"Modified: {num}")
num = modify2()
print(f"Moifies: {num}")                #another way to modified
