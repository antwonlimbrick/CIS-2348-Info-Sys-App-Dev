#Antwon Limbrick
#1972657

import csv

user_input = input()

with open(user_input, 'r') as wordsfile:
    word_reader = csv.reader(wordsfile)
    
    for row in word_reader:
        list_words = row

duplicates = list(dict.fromkeys(list_words))
list_length = len(duplicates)

for i in range(list_length):
    print(duplicates[i], list_words.count(duplicates[i]))
    
    