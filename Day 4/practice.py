#randomisation & modules
import random
import practiceModule

a = 1
b = 10

print("\n")
print(random.randint(a, b))     #prints random integer
print(practiceModule.pi)        #how a module is used
print(random.random() * 5)      #prints a random float number
print("\n")

#lists
list = ["ellyza", "eduardo", "dfjidf", "dfsdfadf"]
print(list)                                         #prints the whole list
print(list[1])                                      #prints an  iten in the list
list[3] = "hi"                                      #changes an intem to the list
print(list)
list.append("hello")                                #adds an item to the end of the list
list[3] = "hi"                                      #changes an intem to the list
print(list)
list.extend(["goodbye", "goodmorning"])             #extends the list
print(list)
print(random.choice(list))                          #picks one item from the list
print("\n")

#nested lists
letters = ["a", "b", "c", "d", "e"]
words = ["yes", "naur", "maybe", "sometimes", "oftenties"]

nest = [letters, words]                                     #combines two lists
print(nest)
print(nest[0][1])                                           #prints an item in a certain list
print(random.choice(letters))                               #chooses an item from the list