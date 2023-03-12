from art import logo
import os
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def rCards(list):
    while len(list) < 2:
        aCards(list)

    check = adding(list)

    if check > 20:
        for i in range(len(list)):
            if list[i] == 11:
                list[i] = 1
            else:
                list[i] = list[i]
    return list

def aCards(list):
    list.append(random.choice(cards))

def adding(list):
    i = 0
    for number in list:
        i += number

    return i

def iPrint(list1, list2, sum1):
    print(f"Your cards: {list1}, current score: {sum1}")
    print(f"Computer's first card: {list2[0]}")

def fPrint(list1, list2, sum1, sum2):
    print(f"Your final hand: {list1}, your final score: {sum1}")
    print(f"Computer's final hand: {list2}, final score: {sum2}")

def check(list1, list2, sum1, sum2, prompt):
    if sum1 == sum2:
        fPrint(list1, list2, sum1, sum2)
        print("Draw!")
    elif sum1 > 21 or (prompt == "n" and sum1 < sum2):
        fPrint(list1, list2, sum1, sum2)
        print("You loose!")
    elif sum1 == 21:
        fPrint(list1, list2, sum1, sum2)
        print("You win!")


def game():

    print(logo)
    uCard = []
    cCard = []
        
    rCards(uCard)
    rCards(cCard)
    sum_uCard = adding(uCard)
    sum_cCard = adding(cCard)

    while not :
        iPrint(uCard, cCard, sum_uCard)
    
        prompt = input("Type 'y' to get another card, type 'n' to pass: ")

            while prompt == "y":
            cards[0] = 1
            aCards(uCard)
            sum_uCard = adding(uCard)
            iPrint(uCard, cCard, sum_uCard)
        
        
    check(uCard, cCard, sum_uCard, sum_cCard, prompt)

game()
