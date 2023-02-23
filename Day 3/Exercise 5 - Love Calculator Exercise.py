# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names = name1 + name2
names = names.lower()

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")
l = names.count("l")
o = names.count("o")
v = names.count("v")

true = str(t + r + u + e)
love = str(l + o + v + e)

score = int(true + love)

if score <= 10 or score >= 90:
    result = ", you go together like coke and mentos."
elif score >= 40 and score <= 50:
    result = ", you are alright together."
else:
    result = "."

print(f"Your score is {score}{result}")