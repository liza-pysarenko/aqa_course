 # task 1

 # a
def is_palindrome(word):

    if word == word[::-1]:
        return '+'
    else:
        return '-'

word = input("Input the word: ")
print(is_palindrome(word))

 # b
def is_palindrome(word):

    if list(word) == list(word)[::-1]:
        return '+'
    else:
        return '-'

word = input("Input the word: ")
print(is_palindrome(word))

 # task 2

def find_word(text, word):

    if word in text:
        return 'YES'
    else:
        return 'NO'

text = input("Input text: ")
word = input("Input word: ")
print(find_word(text, word))

 # task 3

def validate_mail(mail):

    if "@" and "." in mail:
        return 'YES'
    else:
        return 'NO'

mail = input("Input your mail: ")
print(validate_mail(mail))

 # task 4

def last_three_symbols(text_to_list):
    if len(text_to_list) < 3:
        print("The amount of symbols is less than 3:", len(text_to_list))
    else:
        print("The remaining three items on the list:", text_to_list[-3:])

text = input("Input your text: ")
text_to_list = text.split()

print(last_three_symbols(text_to_list))
