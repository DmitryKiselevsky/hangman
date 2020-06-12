#-------------------------------------------------------------------------------
# Name:        hangman
# Purpose:
#
# Author:      D.Kiselevsky
#
# Created:     26.05.2020
# Copyright:   (c) D.Kiselevsky 2020
# Licence:     GPL
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import random

print('H A N G M A N\n')
def game_cycle():
    wordlist = ['python', 'java', 'kotlin', 'javascript']
    guessed = random.choice(wordlist)
    userletters = []
    typed = []
    attempts = 8
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    while attempts > 0:
        hyphens = ''
        for i in range(len(guessed)):
            if guessed[i] in set(userletters):
                hyphens += guessed[i]
            else:
                hyphens += '-'
        print(f'\n{hyphens}')
        letter = input('Input a letter:')
        if len(letter) != 1:
            print('You should input a single letter')
        else:
            if not (str(letter).islower() and str(letter) in set(alphabet)):
                print('It is not an ASCII lowercase letter')
            else:
                if letter in set(typed):
                    print('You already typed this letter')
                else:
                    if letter in guessed:
                            userletters.append(letter)
                    else:
                        attempts -= 1
                        print('No such letter in the word')
                    typed.append(letter)
        if (set(userletters) == set(guessed)):
            attempts = 0
            print(f'\n{guessed}\nYou guessed the word!\nYou survived!\n')
        if attempts == 0 and not (set(userletters) == set(guessed)):
            print('You are hanged!\n')
command_line = input('Type "play" to play the game, "exit" to quit:')
while command_line != 'exit':
    if command_line == 'play':
        game_cycle()
    command_line = input('Type "play" to play the game, "exit" to quit:')
