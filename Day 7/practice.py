#importing
from hangman_art import logo
print(logo)
print("\n")

#list to string
display = ["d", "i", "s", "p", "l", "a", "y"]
print(''.join(display))

#clearing the shell
import os
prompt = input("Type c to clear: ")
if prompt is "c":
    os.system('cls')
else:
    print("Not clear")