#conditional operations
height = 1000                             #assigning a value to a variable
if height >= 120:                       #if statement
    print("above and equal to 120")     #print if true
else:                                   #else statement for trapping
    print("below 120")                  #print if false
print(7 % 2)                            #gets the remainder of a value
print("\n")

#nested if statements
age = 19
if height > 100:
    print("above 100")
    if age <= 18:
        print("below and equal to 18")
    else:
        print("above 18")
else:
    print("below 100")
print("\n")

#elif condition
if height > 100:
    print("above 100")
    if age < 12:
        print("less than 12")
    elif age <= 18:
        print("below and equal to 18")
    elif age == 19:
        print ("is 19")
    else:
        print("above 18")
else:
    print("below 100")
print("\n")