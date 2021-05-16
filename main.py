"""
A Simple calculator CLI tool coded in Python for simple calculations.

This calculator tool can do Addition, Substraction, Multiply, Divide.

Author : Nimish Garg (https://github.com/InsaneTom2005)
Created on : May 16, 2021

last modified by : Lucky verma (https://guthub.com/luckyverma-sudo)
on : May 16, 2021

Changes made in last modification:
1. Changed all old code.

Authors contributed to this script (Add your name below if you have contributed) :
1. Nimish garg (github:https://github.com/InsaneTom2005, email: @gmail.com)
2. Lucky Verma (github:https://github.com/luckyverma-sudo/, email:luckyv0545746@gmail.com)
"""
# Importing required modules
import time

# welcome messages
print("Hello sir!\n")
time.sleep(1)
user_name = input("Please enter your name : ")
print("\n")
print(f"welcome {user_name}!\n")
time.sleep(1)

# definig calculation function
def calc():
    print("\n")
    print("Please choose any operation for your calculation -\n")
    time.sleep(2)
    print("[1] Addition (+)\n[2] Substraction (-)\n[3] Multiply (*)\n[4] Divide (/)\n")

    operation = int(input("Operation : "))
    print("\n")
    time.sleep(1) 

    # main algorithm of tool
    if (operation == 1):
        digit_1 = int(input("Enter the first digit : "))
        print("\n")
        digit_2 = int(input("Enter the second digit : "))
        print("\n")
        sum = digit_1 + digit_2
        print(f"Sum of {digit_1} and {digit_2} : {sum}")

    elif (operation == 2):
        digit_1 = int(input("Enter the first digit : "))
        print("\n")
        digit_2 = int(input("Enter the second digit : "))
        print("\n")
        substraction = digit_1 - digit_2
        print(f"Substraction of {digit_1} and {digit_2} : {substraction}")

    elif (operation == 3):
        digit_1 = int(input("Enter the first digit : "))
        print("\n")
        digit_2 = int(input("Enter the second digit : "))
        print("\n")
        product = digit_1 * digit_2
        print(f"Product of {digit_1} and {digit_2} : {product}")

    elif (operation == 4):
        digit_1 = int(input("Enter the first digit : "))
        print("\n")
        digit_2 = int(input("Enter the second digit : "))
        print("\n")
        divide = digit_1 / digit_2
        print(f"Dividation of {digit_1} and {digit_2} : {divide}")

    else :
        print("[ERROR] : Invalid operation choosed!")
    
    print("\n")
    time.sleep(1)
    thankgiving = f"{user_name}, thank you to choose our Calculator!"
    return thankgiving

# defining function for again run our calculator
def again():
    print("\n")
    yes_no = input("Do you want to use our Calculator again? [y] or [n] : ")

    if (yes_no == "y") or (yes_no == "Y"):
        print(calc())

    elif (yes_no == "n") or (yes_no == "N"):
        print("\n")
        print(f"Ok {user_name},as your wish!")
        exit()

    else :
        print("[ERROR] : wrong choice!")
    print("\n")

# Printing functions
print(calc())

print(again())
print("\n")

print(again())
print("\n")

print(again())
print("\n")

"""                                       ***END***                                          """
