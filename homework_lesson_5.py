# task 1

import math

class NegativeNumberError(Exception):
    pass

try:
    input = float(input("Please input number: "))
    if input < 0:
        raise NegativeNumberError("The square root of a negative number cannot be calculated.")
    square_root = math.sqrt(input)
except ValueError as error:
    print(f"Error: {error}")
except NegativeNumberError as error:
    print(f"Error: {error}")
else:
    print(f"The square root of a number {input} is equal to {square_root:.2f}")
finally:
    print("The calculation is finished.")


# task 2

import math

class NegativeNumberError(Exception):
    pass

try:
    input = float(input("Please input number: "))
    if input < 0:
        raise NegativeNumberError("The square root of a negative number cannot be calculated.")
    square_root = math.sqrt(input)
except ValueError as error:
    print(f"Error: '{error}' is not a number or contains invalid symbols.")
except NegativeNumberError as error:
    print(f"Error: {error}")
except Exception:
    print(f"Something went wrong.")
else:
    print(f"The square root of a number {input} is equal to {square_root:.2f}")
finally:
    print("The calculation is finished.")


# task 3

def calculator():
    while True:
        try:
            num1 = input("Enter the first number (or 'stop' to exit): ")
            if num1 == 'stop':
                print("The calculation is finished.")
                break

            num1 = float(num1)
            operator = input("Enter an arithmetic operation (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Division by zero is impossible!")
                    continue
                result = num1 / num2
            else:
                print("Incorrect operation.")
                continue

            print(f"The result is {result}")
        except ValueError:
            print("Please enter valid values.")


if __name__ == "__main__":
    calculator()

