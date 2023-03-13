from art import logo
import random

def rNum():
    print("I'm thinking of a number between 1 and 100.")
    num = random.randint(1, 101)
    print(num)
    return num

def difficulty():
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return diff

def cDifficulty(diff):
    if diff == "easy":
        tries = 10
    else:
        tries = 5
    return tries

def guess():
    gNum = int(input("Make a guess: "))
    return gNum

def check(gNum, rNum, tries):
    if gNum > rNum:
        print("Too high.")
    elif gNum < rNum:
        print("Too low.")
    else:
        print(f"You got it! The answer was {rNum}")
        over = True
        return over
    
    if tries == 1:
        print("You've run out of guesses, you lose.")
        over = True
        return over

def attempt(count, tries, rNum):
    print(f"You have {tries} attempts remaining to guess the number.")
    gNum = guess()
    over = check(gNum, rNum, tries)
    return over

print(logo)
print("Welcome to the Number Guessing Game!")
random_Num = rNum()
level_difficulty = difficulty()
tries = cDifficulty(level_difficulty)
count = 0
index = tries
over = False

while not over:
    over = attempt(count, index, random_Num)
    count += 1
    index -= 1