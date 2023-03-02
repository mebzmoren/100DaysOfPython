#functions with inputs
def greet():
    print("hi")
    print("hey")
    print("hello")

greet()

def greetName(name):
    print(f"hi, {name}")
    print(f"hey, {name}")
    print(f"hey, {name}")

greetName("Ellyza")
print("\n")

#functions with two arguements
def greetNameLocation(name, location):
    print(f"hi, {name}")
    print(f"hey, {name}")
    print(f"hey, {name}")
    print(f"from {location}")

greetNameLocation("Ellyza", "Sibulan")

def greetWith(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greetWith("Ellyza", "Sibulan")
greetWith("Sibulan", "Ellyza")
print("\n")

#Keyword arguement
greetWith(location = "Sibulan", name = "Ellyza")
print("\n")

#math module
import math

print(math.ceil(3.2))   #rounds up a number