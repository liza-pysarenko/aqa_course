# task 1

def sum_range(start, end):
    if start > end:
        start, end = end, start

    numbers = list(range(start, end + 1))

    total = sum(numbers)
    return total

start = int(input("Input your first number: "))
end = int(input("Input your second number: "))

result = sum_range(start, end)
print(f"The sum of integers from {start} to {end} is {result}.")


# task 2

import math

def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = math.sqrt(2) * side
    return perimeter, area, diagonal

side = float(input("Input the side length of the square: "))
perimeter, area, diagonal = square(side)

print("Perimeter of a square is ", perimeter)
print("Area of a square is ", area)
print("Diagonal of a square is ", diagonal)


# task 3

def get_user_input():
    user_input = input("Please enter a value: ")
    return user_input

def process_input(data):
    try:
        if isinstance(eval(data), str):
            print("User is going to work with string")
        elif isinstance(eval(data), int):
            print("User is going to work with integer")
        elif isinstance(eval(data), float):
            print("User is going to work with float")
        elif isinstance(eval(data), dict):
            print("User is going to work with dictionary")
        elif isinstance(eval(data), list):
            print("User is going to work with list")
        elif isinstance(eval(data), tuple):
            print("User is going to work with tuple")
        else:
            print("User is going to work with unknown data type")
    except Exception as e:
        print(f"Error: {e}")

user_data = get_user_input()

process_input(user_data)
