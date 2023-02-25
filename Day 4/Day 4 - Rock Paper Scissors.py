import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hands = [rock, paper, scissors]
human = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n"))

if human > 2:
    print("You typed an invalid number, you lose!")
else:
    print(hands[human])
    print("Computer chose:")
    computer = random.randint(0,2)
    print(hands[computer])

    if (human == 0 and computer == 2) or (human == 1 and computer == 0) or (human == 3 and computer == 1):
        print ("You win.")
    elif (human == 0 and computer == 1) or (human == 1 and computer == 2) or (human == 3 and computer == 0):
        print("You loose.")
    else:
        print("Draw.")