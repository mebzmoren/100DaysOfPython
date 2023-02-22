#printing
print("Hello world!")   #prints hello world on the terminal/console, these are known as strings

print('print("hi")hi')  #if you want to print double quotes
print('hi')             #single quotes can be used to determine a string instead of a double quote

#breaking a line
print("hello\nworld")       #can print out 2 lines of strings for one line of code
print("hello\nworld\n")     #can add a new blank line to print
print("hello" + "mebz")     #combines 2 strings, no space in between
print("hello " + "mebz")    #combines 2 strings

#inputs
input("input: ")                #accepts an input
print(input("input: ") + "!")   #nested, accepts an input then prints the input & strings together

#len function
s = 'hehe'      #assigns a value to s
print(len(s))   #gets the length of s then prints the length

#variables
name = input("what is your name? ") #assigns the input to a variable
print(name)                         #prints what is stored in the variable
name2 = "hello world"               #assigns a string to a variable
print(name2)                        #prints what is stored in the variable
name2 = "hihihi"                    #added another string to the same variable
print(name2)                        #prints the new string

name3 = input("input")  #accepts input and stores it in a variable
length = len(name3)     #gets the lenth of the input and stores it in a variable
print(length)           #prints the lenth of the input
