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
print("\n")

#nesting lists & dictionaries
travels = {                                                                             #nesting a list in a dictionary
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}
print(travels)                                                                          #nesting a list in a list
letters = ["a", "b", ["c", "d"]]
print(letters)
newTravels = {                                                                          #nesting a dictionary in a dictionary
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 1},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 3}
}
print(newTravels)
newTravels1 = [                                                                         #nesting a dictionary in a list
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 1
    },
    {
        "country":"Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 3
    }
]
print(newTravels1)