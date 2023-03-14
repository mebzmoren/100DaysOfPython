import os
import random
import art
from game_data import data

info = []

def randomize(list):
    list.append(random.choice(data))

def generate(list):
    while len(list) < 2:
        randomize(list)

def display(list, index):
    print(f"Compare A: {list[index]['name']}, a {list[index]['description']}, from {list[index]['country']}")

def answer():
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if choice == "A":
        return 0
    else:
        return 1

def check(list, index1, index2):
    score = 0
    if list[index1]['follower_count'] > list[index2]['follower_count']:
        score += 1
        return score
    
def assignment(choice):
    if choice == 0:
        return 1
    else:
        return 0

print(art.logo)
generate(info)
display(info, 0)
print(art.vs)
display(info, 1)
choice = answer()
other = assignment(choice)
score = check(info, choice, other)

