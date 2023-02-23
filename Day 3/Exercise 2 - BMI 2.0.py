# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight / (height ** 2)

if BMI <= 18.5:
    condition = "are underwheight."
elif BMI <= 25:
    condition = "have a normal weight."
elif BMI <= 30:
    condition = "are slightly overweight."
elif BMI <= 35:
    condition = "are obese."
else:
    condition = "clinically obese."

print(f"Your BMI is {round(BMI)}, you {condition}")