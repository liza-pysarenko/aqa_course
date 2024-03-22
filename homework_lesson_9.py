# task 1

def my_generator(start: int, stop: int, step: int = 5):
    value = start
    while value < stop:
        yield value
        value += step

for index in my_generator(0, 20):
    print(index)


# task 2

generator_comp = (i for i in range(1, 11))

for result in generator_comp:
    print(result)
