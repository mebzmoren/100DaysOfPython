print("Welcome to the tip calculator.")
tBill = float(input("What was your total bill? $"))
tPercentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
nPeople = int(input("How many people to split the bill? "))
tip = (tBill + (tPercentage/100)*tBill) / nPeople
print(f"Each person should pay: ${round(tip, 2)}")