#dictionaries
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.", 
    "Loop": "The action of doing something over and over again."
}
print(programming_dictionary["Bug"])                                                    #retrieve items from dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."   #add items to dictionary
print(programming_dictionary)
programming_dictionary["Bug"] = "edited"                                                #to edit a value of a key
print(programming_dictionary)
for key in programming_dictionary:
    print(key)                                                                          #will only print the key if looped
    print(programming_dictionary[key])                                                  #will only print the value
newDictionary = {}                                                                      #empty dicionary
programming_dictionary = {}                                                             #to wipe a dictionary
print(programming_dictionary)