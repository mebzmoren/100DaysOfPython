#function with outputs
def something():
    result = 3 * 2
    return result                               #returns the value of the variable

print(something())                              #prints returned value
print("hehe".title())                           #converts the 1st letter of the words into upper case

def formating(fName, lName):
    if fName == "" or lName =="":
        return                                  #terminates the function
    name = fName.title() + " " + lName.title()
    return name

print(formating("ellyza", "papas"))
print("\n")
