#for loops
fruits = ["Apple", "Peach", "Pear"] 
for fruit in fruits:                #will individually print the items in a list
    print(fruit)
    print(fruit + " Pie")           #will add another word to the items in a list
print(fruits)                       #will print the whole list once after the loop
print("\n")

#split
strings = "I, a 22 year old girl, is doing this challenge".split()          #spilts the string word by word
print(strings)
newStrings = "I, a 22 year old girl, is doing this challenge".split(", ")   #splits by every comma
print(newStrings)
print("\n")

#sum
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))         #prints the sum of a list of integers
print("\n")

#min max
print(min(numbers)) #prints out the minimum number of the list
print(max(numbers)) #prints out the maximum number of the list
print("\n")

#range
x = range(3)                        #prints out the range of numbers from 0 to n - 1
for n in x:
    print(n)
print("\n")
for newNumber in range(1, 10):      #another way to write
    print(newNumber)
print("\n")
for newNumbers in range(1, 11, 3):  #prints out the range of numbers wit steps
    print(newNumbers)
print("\n")
total = 0
for adding in range(1, 101):
    total += adding
print(total)