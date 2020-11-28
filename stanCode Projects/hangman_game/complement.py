"""
File: complement.py
Name: Charlie Liu
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    step 1 - input dna data
    step 2 - transfer into capital letter
    step 3 - find the complement of import dna data and print the complement data
    """
    dna_data = input('Please give me a DNA strand and I\'ll find the complement : ')
    dna = dna_data.upper()
    print('The complement of ' + str(dna) + ' is ' + build_complement(dna))


def build_complement(dna):
    """
    find the complement of the input dna data
    The complement of A is T
    The complement of T is A
    The complement of C is G
    The complement of G is C
    :param dna: is string, the import of dna data
    :return: is string, the complement of the import dna data
    """
    ans = ''
    for i in dna:         # for character in the dna data
        if i == 'A':      # if one of the dna data is A
            ans += 'T'    # the complement of A is T
        elif i == 'T':    # if one of the dna data is T
            ans += 'A'    # the complement of T is A
        elif i == 'C':    # if one of the dna data is C
            ans += 'G'    # the complement of C is G
        elif i == 'G':    # if one of the dna data is G
            ans += 'C'    # the complement of G is C
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
