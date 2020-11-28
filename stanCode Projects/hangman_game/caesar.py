"""
File: caesar.py
Name: Charlie Liu
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    STEP 1 - get the secret number
    STEP 2 - get the ciphered string
    STEP 3 - use the secret number to reconstruct the new alphabet
    STEP 4 - solve the ciphered string
    STEP 5 - print the result
    """
    shift_step = int(input('Secret Number is : '))
    secret = input('What\'s the ciphered string ')
    secret_cap = secret.upper()   # transfer into capital character
    new_alphabet = ALPHABET[(len(ALPHABET)-shift_step):]+ALPHABET[:(len(ALPHABET)-shift_step)]
    """
    based on the secret number, we can shift the alphabet sequence to get the new alphabet sequence
    """
    secret_solve = caesar_secret(secret, new_alphabet, secret_cap)
    print(secret_solve)


def caesar_secret(secret, new_alphabet, secret_cap):
    """
    if the character in the secret_cap and new_alphabet is same, use the index system to pick the same index in alphabet
    and renew the secret_solve
    :param secret: is string, the ciphered string
    :param new_alphabet: the new alphabet order we change based on the secret number
    :param secret_cap: the secret word we input with capital character
    :return: string, the answer of ciphered string
    """
    secret_solve = ''
    for i in range(len(secret)):
        for j in range(len(new_alphabet)):
            if secret_cap[i] == new_alphabet[j]:              # secret_cap equal new_alphabet
                secret_solve = secret_solve + ALPHABET[j]     # use the index find the word in alphabet and renew
            elif secret_cap[i] == ' ':                        # if we have empty string like space
                secret_solve = secret_solve + str(' ')        # just direct add it for once
                break
            elif new_alphabet.find(secret_cap[i]) == -1:      # if we can't find the sting, it might be special, like !
                secret_solve = secret_solve + secret_cap[i]   # also direct add it once
                break
    return secret_solve                                       # return secret_solve, the answer


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
