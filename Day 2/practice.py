#data types
print("hello"[0])   #subscripting:  prints the first character of the string, programs always start counting from 0
print("123" + "4")  #numbers enclosed in double quotes are treated as a string
print(123)          #prints an integer
print(123 + 4)      #adds up two numbers
print(1_000_000)    #underscore splits large numbers to be readable but won't be printed together with the number
print(3.14)         #prints a float
print(True)         #prints a boolean data type

#avoiding errors when it comes to data types
name = len(input("Input: "))                    #accepts an input and stores it in a variable
print(type(name))                               #prints the data type of the variable
newName = str(name)                             #typecasting: changes the data type, converted integer into string
print("Input has " + newName + " characters.")  #prints the length of the input
a = float(1234)                                 #converts integer into float
print(type(a))                                  #prints data type of a variable
print(70 + float("100.5"))                      #converts string into float and adds an integer
print(str(70) + str("100"))                     #converted into string and is concatenated

#mathematical operations
print(1 + 1)            #addition
print(3 - 1)            #subtraction
print(2 * 1)            #multiplication
print(4 / 2)            #division, output will always be a float'
print(4 ** 2)           #exponent
print(1 * 2 - 1 / 3)    #PEMDASLR

#number manipulation
print(round(8 / 3, 2))          #rounds float
print(8 // 3)                   #converts float into integer
result = 0                      #assigns a value to an variable
result += 1                     #manipulates previous value
print(result)                   #prints new result
print(f"result is {result}")    #f-string: combines string with different data types