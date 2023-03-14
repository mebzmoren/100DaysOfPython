import os
import random
import art
from game_data import data

info = []
over = False
score = 0

def randomize(list):
    list.append(random.choice(data))

def generate(list):
    while len(list) < 2:
        randomize(list)

def display(list, index, part):
    print(f"Compare {part}: {list[index]['name']}, a {list[index]['description']}, from {list[index]['country']}")

def answer():
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if choice == "A":
        return 0
    else:
        return 1
    
def assignment(choice):
    if choice == 0:
        return 1
    else:
        return 0
    
def check(list, index1, index2, score):
    if list[index1]['follower_count'] > list[index2]['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}")
        return False
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        return True


while not over:
    print(art.logo)
    generate(info)
    display(info, 0, "A")
    print(art.vs)
    display(info, 1, "B")
    choice = answer()
    other = assignment(choice)
    os.system('cls')
    over = check(info, choice, other, score)