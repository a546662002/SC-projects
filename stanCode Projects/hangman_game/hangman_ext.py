"""
File: hangman.py
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    Step 1 - set the dashed string base on the random word
    Step 2 - input your guess
    Step 3 - if correct, renew the dashed string with word
    Step 4 - if wrong, do not renew, and plus one mistake
    Step 5 - totally hung or find the word
    """
    answer = random_word()
    dashed = ''                                           # based on the random word to build the length of dash
    for i in range(len(answer)):
        dashed = dashed + '-'
    print('The word looks like '+dashed)
    print('You have ' + str(N_TURNS) + ' guesses left.')
    mistake = 0                                           # record the how many mistake we made
    win_indiate = '-'                                     # if there is not dash in string, mean we find the word
    while N_TURNS > mistake:
        if dashed.find(win_indiate) == -1:                # check if we find the word or there still dash in it
            break
        input_ch = input('Your guess:')
        input_checked = input_check(input_ch)             # check the input is correct
        new_input_ch = input_checked.upper()              # transfer input into capital character

        if answer.find(new_input_ch) == -1:               # if input is not in the answer
            mistake = mistake + 1                         # mistake plus one
            hangman_pic(mistake)                          # draw the picture
            print('There is no '+str(new_input_ch)+'\'s in the word')
            if (N_TURNS-mistake) != 0:                    # happen if you still have chance to guess
                print('You have '+str(N_TURNS-mistake)+' guesses left')
            else:                                         # happen when you run out your chance
                print('You are completely hung :;(∩´﹏`∩);:')
                print('The word was : '+answer)
        else:                                             # if the input is in the answer
            for i in range(len(answer)):
                if new_input_ch[0] == answer[i]:          # renew the dash string with the input
                    dashed = dashed[:i] + answer[i] + dashed[i + len(new_input_ch):]
            mistake = mistake + 0
            hangman_pic(mistake)                          # draw the picture
            print('You are correct!')
            if dashed.find(win_indiate) != -1:            # if the word is not finish, there still dash in it
                print('The word looks like ' + dashed)    # show the word you guess so far and the chance you left
            if dashed.find(win_indiate) != -1:
                print('You have ' + str(N_TURNS - mistake) + ' guesses left')
    win_check(win_indiate, dashed, answer)                # use the dash to check if we find the word or not




def win_check(win_indiate, dashed, answer):
    """
    if we can not find dash in the original dash string line, and it mean we find the word
    :param win_indiate: string, use to check if there is still dash in it
    :param dashed: string, the word we guess so far
    :param answer: string, the random number word
    """
    if dashed.find(win_indiate) == -1:     # if we can not find the dash, it mean we figure out the word
        print('You win !')
        print('(ﾉ>ω<)ﾉ', end="")
        print('(ﾉ>ω<)ﾉ', end="")
        print('(ﾉ>ω<)ﾉ')
        print('The word was : ' + answer)


def input_check(input_ch):
    """
    to check if the input is correct, one character and not number
    :param input_ch: string, the input is not check
    :return: input_ch, is string, alrady check it is not number in it and only one character
    """
    while True:
        if input_ch.isalpha() != True:       # check if there is number in it
            print('illegal format')
            input_ch = input('Your guess:')
        elif len(input_ch) != 1:             # check if the input is too long or not
            print('illegal format')
            input_ch = input('Your guess:')
        else:
            return input_ch



def hangman_pic(mistake):
    """
    show the hangman based on the ratio of mistake and n_turns so we can adjust the n_turns
    :param mistake: integer, show how many mistake we made
    """
    if mistake/N_TURNS == 0:
        print('|-----')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
    if mistake/N_TURNS > 0 and (mistake/N_TURNS) < 0.17:
        print('|-----|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
    if mistake/N_TURNS >= 0.17 and (mistake/N_TURNS) < 0.34:
        print('|-----|')
        print('|     ○')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
    if mistake/N_TURNS >= 0.34 and (mistake/N_TURNS) < 0.51:
        print('|-----|')
        print('|     ○')
        print('|     |')
        print('|     |')
        print('|')
        print('|')
        print('|')
    if mistake/N_TURNS >= 0.51 and (mistake/N_TURNS) < 0.68:
        print('|-----|')
        print('|     ○')
        print('|    /|')
        print('|   / | ')
        print('|')
        print('|')
        print('|')
    if mistake/N_TURNS >= 0.68 and (mistake/N_TURNS) < 0.85:
        print('|-----|')
        print('|     ○')
        print('|    /|\\')
        print('|   / | \\')
        print('|')
        print('|')
        print('|')
    if mistake/N_TURNS >= 0.85 and (mistake/N_TURNS) < 1:
        print('|-----|')
        print('|     ○')
        print('|    /|\\')
        print('|   / | \\')
        print('|    /')
        print('|   /')
        print('|')
    if mistake == N_TURNS:
        print('|-----|')
        print('|     ○')
        print('|    /|\\')
        print('|   / | \\')
        print('|    / \\')
        print('|   /   \\')
        print('YOU ARE DEAD')


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
