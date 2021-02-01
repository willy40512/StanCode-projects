"""
File: hangman.py
Name: Willie Li
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This is a hangman game which will generate a vocabulary to let the user
    guess. As the guess is wrong, user will lose one life. The game will
    end till the life to zero.
    """
    answer = random_word()
    guess(answer)


def guess(a):
    dash = ''
    # transform the answer to dash
    for i in range(len(a)):
        dash += '-'
    life = N_TURNS
    while life != 0:
        print('The word looks like: ' + dash)
        print('You have ' + str(life) + ' guesses left.')
        input_ch = input('Your guess: ')
        input_ch = input_ch.upper()
        while not input_ch.isalpha():
            print('Illegal format.')
            input_ch = input('Your guess: ')
            input_ch = input_ch.upper()
        while len(input_ch) != 1:
            print('Illegal format.')
            input_ch = input('Your guess: ')
            input_ch = input_ch.upper()
        match = a.find(input_ch)  # the index of the word


        # match the word between input_ch and ans
        for i in range(len(a)):
            if a[i] == input_ch:
                dash1 = dash[:i]+a[i]
                dash = dash1 + dash[i+1:]
            else:
                dash = dash
        # the input did not exist in the ans
        if match == -1:
            life -= 1
            print('There is no ' + input_ch+"'s in the word.")
        else:
            print('You are correct !')

        if life == 0:
            print('You are completely hung ~')
            print('The word was: ' + a)
        if dash == a:
            print('You win !')
            print('The word was: ' + dash)
            life = life - life


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
