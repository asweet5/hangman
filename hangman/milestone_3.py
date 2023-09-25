import random

word_list = ['apple', 'strawberry', 'banana', 'blackberry', 'raspberry']
word = random.choice(word_list)
print(word)

while True:
    guess = input('Enter a sinlge letter as your guess: ')
    if len(guess) == 1 and guess.isalpha() == True:
        print('Good guess')
        break
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')

if guess in word:
    print(f'Good guess! {guess} is in the word.')
else:
    print(f'Sorry {guess} is not in the word try again.')