# task 1

import time


def decorator_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return result, execution_time

    return wrapper


@decorator_time
def my_func(n):
    time.sleep(n)
    return f"Function executed after {n} seconds"


result, time_taken = my_func(5)
print("Result:", result)
print("Time taken:", time_taken)

# task 2

def logger(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(message)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@logger('This function will capitalize a string')
def capitalize_string(s):
    return s.capitalize()


result = capitalize_string("hello, world!")
print(result)
