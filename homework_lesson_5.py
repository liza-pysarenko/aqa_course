# task 1

import math

try:
    input = float(input("Please input number: "))
    if input < 0:
        raise ValueError("The square root of a negative number cannot be calculated.")
    square_root = math.sqrt(input)
except ValueError as error:
    print(f"Error: {error}")
else:
    print(f"The square root of a number {input} is equal to {square_root:.2f}")
finally:
    print("The calculation is finished.")


# task 2

import math

try:
    input = float(input("Please input number: "))
    if input < 0:
        raise ValueError("The square root of a negative number cannot be calculated.")  # не можу зрозуміти, що не так, бо коли ввожу мінусове число, то отримую одразу дві помилки "Error: 'The square root of a negative number cannot be calculated.' is not a number or contains invalid symbols."
    square_root = math.sqrt(input)
except ValueError as error:
    print(f"Error: '{error}' is not a number or contains invalid symbols.")
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
            num1 = float(input("Enter the first number (or 'stop' to exit): "))
            if num1 == 'stop':
                print("The calculation is finished.")
                break  # і тут не можу зрозуміти де помилка і чому вводячи stop я перехожу в Please enter valid values і знову в "Enter the first number (or 'stop' to exit): "

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


