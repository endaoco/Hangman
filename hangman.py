import random
import os
import sys

words = [
    'bowl',
    'cheese',
    'burger',
    'lime',
    'churro',
    'blackberry',
    'moon',
    'spontaneous']

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def draw(bad_guesses, good_guesses, secret_word):
    clear()

    print('')
    print('strikes: {}/7'.format(len(bad_guesses)))

    for letter in bad_guesses:
        print(letter, end=' ')
    print('\n\n')

    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end=' ')
        else:
            print('_ ', end=' ')
    print('')

def get_guess(bad_guesses, good_guesses):
    while True:
        guess = input('Choose a letter from a-z: ').lower()

        if len(guess) != 1:
            print('You can only guess one letter!')
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that letter")
        elif not guess.isalpha():
            print('Only letters please')
        else:
            return guess

def play(done):
    clear()
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []
    win = False

    while True:

        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses, good_guesses)

        if guess in secret_word:
            good_guesses.append(guess)
            win = True
            for letter in secret_word:
                if letter not in good_guesses:
                    win = False
        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, secret_word)
                print('You lose!')
                print('The secret word was {}'.format(secret_word))
                done = True
        if win:
            print('You win!')
            print('The secret word was {}'.format(secret_word))
            done = True

        if done:
            play_again = input('Play again? Y/N ').lower()
            if play_again != 'n':
                return play(done=False)
            else:
                print('Bye!')
                sys.exit()

def welcome():
    start = input('Press enter/return to start or Q to quit').lower()
    if start == 'q':
        print('Bye!')
        sys.exit()
    else:
        return True

print('Welcome to hangman')

done = False

while True:
    clear()
    welcome()
    play(done)

