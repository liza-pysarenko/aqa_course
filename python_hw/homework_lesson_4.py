# task 1

names = ["john", "marta", "james", "amanda", "marianna"]
capitalized_names = [name.title() for name in names]

print(capitalized_names)


# task 2

import re

camel_case_list = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_list = []

for items in camel_case_list:
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', items).lower()
    snake_case_list.append(snake_case)

print(snake_case_list)


# task 3

language_developer_dict = {'Python': 'Guido Van Rossum', 'C++': 'Bjarne Stroustrup', 'Java': 'James Gosling', 'Java Script': 'Brendan Eich'}

for language, developer in language_developer_dict.items():
    print(f"My favorite programming language is {language}, which was created by {developer}.")

del language_developer_dict['Java Script']

print(language_developer_dict)


# task 4

names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']

for list in names:
    if not isinstance(list, str):
        continue
    print(list)


# task 5

types = [1, 1000, 2, 12, {'key': 'value'}]

for item in types:
    if type(item) != int:
        print(f"The loop is not working with {type(item)} data type.")
        break
    print(item)


# task 6

new_input = input("Please input smth: ")

char_count = {}

for char in new_input:
    char_count[char] = char_count.get(char, 0) + 1

result = ", ".join([f"{char},{count}" for char, count in char_count.items()])
print(result)