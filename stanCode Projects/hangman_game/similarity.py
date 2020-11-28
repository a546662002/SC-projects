"""
File: similarity.py
Name: Charlie Liu
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    STEP 1 - input dna data, including the sequence and the part you want to match
    STEP 2 - Transfer these data into capital character
    STEP 3 - find the best match part in the sequence and print
    """
    dna_input = input('Please give me a DNA sequence : ')
    dna_seq = dna_input.upper()                                       # transfer dna_input in to capital character
    dna_data = input('What DNA sequence would you like to match : ')
    dna_match = dna_data.upper()                                      # transfer dna_data in to capital character
    dna_seq_len = len(dna_seq)                                        # get the length of dna_sequence
    dna_match_len = len(dna_match)                                    # get the length of the part you want to match
    print('The best match is ' + similarity(dna_match, dna_seq, dna_seq_len, dna_match_len))


def similarity(dna_match, dna_seq, dna_seq_len, dna_match_len):
    """
    Based on the dna_match_length, use this length to pick the same length dna data from the dna_seq, include all the
    possibility in the dna_seq, and compare these possibility to find the max similarity
    :param dna_match: is string, dna part you want to match
    :param dna_seq: is string, the dna sequence you input
    :param dna_seq_len: is integer, the length of dna sequence you input
    :param dna_match_len: is integer, the length of dna data you want to match
    :return: the best similarity in the dna sequence
    """
    best_percent = 0
    best_match = ''
    for i in range(dna_seq_len-dna_match_len+1):
        """
        Based on the length of dna data you want to match, there will have dna_seq_len-dna_match_len+1 possibility
        """
        correct = 0
        total = 0
        pick = dna_seq[i:i+dna_match_len]  # pick every possibility to compare
        for j in range(dna_match_len):
            if pick[j] == dna_match[j]:    # if match, use correct and total to calculate percent of correct
                correct += 1
                total += 1
            else:
                total += 1
        percent = correct/total
        if percent > best_percent:
            """
            if percent is bigger than best percent, it means this possibility will be the best similarity
            """
            best_percent = percent
            best_match = pick
    return best_match                      # best match is the answer with highest similarity


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
