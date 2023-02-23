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

#multiple if statements
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

    decicion = "Y"
    if decicion == ("Y"or "y"):
        print("\nyes")
else:
    print("below 100")
print("\n")

#logical operators
a = 12
print(a > 15)
print(a > 10 and a < 13)
print(a > 15 and a < 13)
print(not a > 15)
low = "Ellyza".lower()
print(low.count("l"))
print("\n")

#