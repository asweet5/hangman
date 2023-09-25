import random
import string

word_list = ['apple', 'strawberry', 'banana', 'blackberry', 'raspberry']
word = random.choice(word_list)
print(word)

guess = input("Please enter a single letter as your guess: ")
if len(guess) == 1 and guess in string.ascii_letters:
    print("Good guess!")
else:
    print("Opps! That's not a valid input")