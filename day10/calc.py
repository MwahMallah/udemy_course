def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

import os

def calculator():
    first_num = float(input("What's the first number?: "))
    should_continue = True

    while should_continue:
        operation = input("What's the operation: ")
        next_num = float(input("What's the next number?: "))

        answer = operations[operation](first_num, next_num)

        print(f"{first_num} {operation} {next_num} = {answer}")

        if input("Enter 'y' to continue: ") == 'y':
            first_num = answer

        else: 
            should_continue = False
            os.system("clear")
            calculator()
            

calculator()