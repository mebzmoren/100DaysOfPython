def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number?: "))
    prompt = "y"

    for operation in operations:
        print(operation)

    while prompt == "y":
        operator = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        funct = operations[operator]
        answer = funct(num1, num2)

        print(f"{num1} {operator} {num2} = {answer}")

        prompt = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        
        if prompt == "y":
            num1 = answer
        else:
            calculator()
    
    return prompt

from art import logo
print(logo)
calculator()