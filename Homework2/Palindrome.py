#Antwon Limbrick
#1972657

input_word = str(input())

user_word = input_word

user_word = user_word.replace(" ", "")

new_word = user_word

new_word = new_word[::-1]


if user_word == new_word:
    print("{} is a palindrome".format(input_word))
else:
    print("{} is not a palindrome".format(input_word))
    
    