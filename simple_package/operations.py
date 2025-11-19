###
## simple_package - Module operations.py
## Basic online calculator
###

## Here I have defined four functions for the four
## basic operations. 
##
## 1) You should provide an interface function
##    that will prompt the user for input and
##    call the appropriate function based on the
##    user's input. The interface function should
##    continue to prompt the user for input until
##    the user enters'exit'. 
##
## 2) The interface function should also handle
##    any exceptions that might be thrown by the
##    basic operations functions. If an exception 
##    is thrown,the interface function should print 
##    an error message and continue to prompt the 
##    user for input.
##
## 3) Add other "operations" to the calculator, that
##    involve complicated operations (e.g., 
##    trigonometric functions, logarithms, etc.).
##

# adding math module for complicated operations
import math 

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract one number from another."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide one number by another."""
    # adding this line for exception handling
        if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

# -------------------------------
# adding more complex operations - adding square root and trigonometric function
# -------------------------------

def sine(a):
   return math.sin(a)

def cosine(a):
   return math.cos(a)

def tangent(a):
   return math.tan(a)

def square_root(a):
   return math.sqrt(a)

# ------------------------------
# adding interface to prompt user for input
# ------------------------------

def run_calculator():
   
    print("Select operation: add, subtract, multiply, divide, sine, cosine, tangent, square_root")
    print("Type 'exit' to quit.\n")

    # mapping command -> function
    operations_two_inputs = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    operations_one_input = {
        "sine": sine,
        "cosine": cosine,
        "tangent": tangent,
        "square_root": square_root,
    }

    while True:
        user_input = input("Enter operation: ").strip().lower()

        if user_input == "exit":
            print("Exiting operations.")
            break

        try:
            # Two-input operations
            if user_input in operations_two_inputs:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = operations_two_inputs[user_input](a, b)

            # One-input operations
            elif user_input in operations_one_input:
                a = float(input("Enter a number: "))
                result = operations_one_input[user_input](a)

            else:
                print("Unknown operation. Try again.")
                continue

            print("Result:", result)

        except Exception as e:
            print("Error:", e)
            print("Please try again.\n")