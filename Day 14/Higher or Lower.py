import os
import random
import art
from game_data import data

over = False
score = 0

def generate():
    list = []
    while len(list) < 2:
        list.append(random.choice(data))

    return list

def display(list, index, part):
    print(f"Compare {part}: {list[index]['name']}, a {list[index]['description']}, from {list[index]['country']}")
    print(f"followers: {list[index]['follower_count']}")

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
        print(art.logo)
        print(f"You're right! Current score: {score}")
        return False
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        return True
    
def clear_screen():
    os.system('cls')
    
if not over:
    print(art.logo)

while not over:
    list = generate()
    display(list, 0, "A")
    print(art.vs)
    display(list, 1, "B")
    choice = answer()
    other = assignment(choice)
    clear_screen()
    over = check(list, choice, other, score)
    if not over:
        score += 1