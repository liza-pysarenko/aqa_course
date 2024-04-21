# task 1

def my_map(func, iterable):
    for item in iterable:
        yield func(item)

def my_filter(func, iterable):
    for item in iterable:
        if func(item):
            yield item

def square(a):
    return a ** 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers = list(my_map(square, numbers))
print(squared_numbers)

def is_even(b):
    return b % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(my_filter(is_even, numbers))
print(even_numbers)


# task 2

def my_func(x):
    return lambda y: y ** x

power_of_2 = my_func(3)
print(power_of_2(4))


# task 3

def print_hi():
    return "Hi"

def print_hello():
    return "Hello"

def print_greetings():
    return "Greetings"

def execute_func(func_name):
    try:
        result = eval(func_name)
        print("Result:", result)
    except NameError:
        print("Function", func_name, "does not exist.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    func_name = input("Enter the function name: ")
    execute_func(func_name)