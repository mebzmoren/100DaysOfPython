# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
tempHeight = float(height)
tempWeight = int(weight)
BMI = tempWeight / tempHeight ** 2
print(int(BMI))
