while True:
    guess = input('Enter a sinlge letter as your guess: ')
    if len(guess) == 1 and guess.isalpha() == True:
        print('Good guess')
        break
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')