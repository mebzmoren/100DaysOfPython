import os
from art import logo

data = {}

def newDictionary(n, p):
    data[n] = p

def hBidder(dictionary):
    temp1 = ""
    temp2 = 0
    for name in dictionary:
        if (dictionary[name]) > temp2:
            temp1 = name
            temp2 = dictionary[name]
    print(f"The winner is {temp1} with a bid of ${temp2}")
    

print(logo)
prompt = "yes"

while prompt == "yes":
    name = input("What is your name?: ")
    bPrice = int(input("What is your bid?: $"))

    newDictionary(name, bPrice)

    prompt = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if prompt == "no":
        hBidder(data)
    else: 
        os.system('cls')

