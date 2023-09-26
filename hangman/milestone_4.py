import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(self.word)
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word")
            for i in range(len(self.word)):
                if guess == self.word[i]:
                    self.word_guessed[i] = guess
                    self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        print(self.word_guessed)

    def ask_for_input(self):
        while True:
            guess = input("Enter a sinlge letter as your guess: ")
            if len(guess) > 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical letter.")
            elif guess in self.list_of_guesses:
                print("You've already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

word_list = ['apple', 'strawberry', 'banana', 'blackberry', 'raspberry']

test = Hangman(word_list)

test.ask_for_input()
