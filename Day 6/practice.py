#functions
def functionOne():  #function for printing strings
    print("Hello")
    print("Bye")

functionOne()       #function is in use
print("\n")

#while loops
again = "y"
while again == "y":                   #will loop if true and will terminate if false
    again = input("again? (y/n): ")
    again.lower()