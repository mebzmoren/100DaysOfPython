# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
tempAge = int(age)
limit = 90
days = 365
weeks = 52
months = 12
daysL = limit * days - tempAge * days
weeksL = limit * weeks - tempAge * weeks
monthsL = limit * months - tempAge * months
print(f"You have {daysL} days, {weeksL} weeks, and {monthsL} months left.")