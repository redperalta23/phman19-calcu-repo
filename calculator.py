# imported sleep module to put delay in display
from time import sleep


# function to add two numbers
def add(number1, number2):
    return float(number1) + float(number2)


# function to subtract two numbers
def subtract(number1, number2):
    return float(number1) - float(number2)


# function to multiply two numbers
# divide function
def multiply(number1, number2):
    return float(number1) * float(number2)


# function to divide two numbers
def divide(number1, number2):
    if float(number2) == 0:  # to handle division by zero error
        print("\nDivision by zero is not allowed.")
        sleep(2)
        exit()
    return float(number1) / float(number2)


# function for exception handling of first number
def exception_for_number1(number1):
    try:
        float(number1)
    except ValueError:
        print(f"\nInvalid input! {number1} is not a number.\n")
        sleep(1.5)
        exit()


# function for exception handling of second number
def exception_for_number2(number2):
    try:
        float(number2)
    except ValueError:
        print(f"\nInvalid input! {number2} is not a number.\n")
        sleep(1.5)
        exit()


# function for the menu
def menu():
    print("*** My Simple Calculator ***")
    print("""
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exit
        """)


# start of loop block
while True:
    menu()  # call the menu function
    option = input("Enter your choice [1 to 5]: ")
    try:  # to handle wrong input of option that is not numeric
        option = int(option)
    except ValueError:
        print(f"\n{option} is an invalid choice. Please enter a number.\n")
        sleep(2)
        continue
    if int(option) == 1:  # if statement for option 1
        first_number = input("\nEnter first number: ")
        exception_for_number1(first_number)
        second_number = input("Enter second number: ")
        exception_for_number2(second_number)
        print(f"\n{first_number} + {second_number} = {add(first_number, second_number)}\n")
        sleep(2)
    elif int(option) == 2:  # if statement for option 2
        first_number = input("\nEnter first number: ")
        exception_for_number1(first_number)
        second_number = input("Enter second number: ")
        exception_for_number2(second_number)
        print(f"\n{first_number} - {second_number} = {subtract(first_number, second_number)}\n")
        sleep(2)
    elif int(option) == 3:  # if statement for option 3
        first_number = input("\nEnter first number: ")
        exception_for_number1(first_number)
        second_number = input("Enter second number: ")
        exception_for_number2(second_number)
        print(f"\n{first_number} * {second_number} = {multiply(first_number, second_number)}\n")
        sleep(2)
    elif int(option) == 4:  # if statement for option 4
        first_number = input("\nEnter first number: ")
        exception_for_number1(first_number)
        second_number = input("Enter second number: ")
        exception_for_number2(second_number)
        print(f"\n{first_number} / {second_number} = {divide(first_number, second_number)}\n")
        sleep(2)
    elif int(option) == 5:  # if statement for option 5
        print("\nExiting program. Bye...")
        break
    else:  # to handle numeric input that is outside the options available
        print(f"\n{option} is not in the options. Choose from 1 to 5 only.\n")
        sleep(2)
