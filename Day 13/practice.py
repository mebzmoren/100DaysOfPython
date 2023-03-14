############DEBUGGING#####################

# Describe Problem
def my_function():
    for i in range(1, 21):          #upper bound should be +1
        if i == 20:
            print("You got in\n")
my_function()

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)                    #range includes both endpoints
print(f"{dice_imgs[dice_num]}\n")

# Play Computer
year = int(input("What's your year of birth?"))
if year >= 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:                              #there must be a condition for 1994
    print("You are a Gen Z.\n")
else:
    print("\n")
    

# Fix the Errors
age = int(input("How old are you?"))        #integer2 inputs must be converted into integers
if age > 18:
    print(f"You can drive at age {age}.\n")    #must be indented & converted into an f string
else:
    print("\n")


#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))    #'==' is only used to compare
total_words = pages * word_per_page
print(f"{total_words}\n")

#Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item) #must be in the for loop
    print(b_list)

mutate([1,2,3,5,8,13])