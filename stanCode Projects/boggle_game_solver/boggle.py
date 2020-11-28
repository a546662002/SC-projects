"""
File: boggle.py
Name: Charlie Liu
----------------------------------------
TODO:
"""
# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# global variable
dic_list = []       # save the word in dictionary
data_list = []      # save the data we input
word_location = []  # save the row and column value of the word because word pass only one time
find_word = []      # the word we found on boggle
is_data_input = True
total = 0           # count the word we found


def main():
	"""
	This algorithm is input four rows of alphabet , then connect to form a word base on your neighbor alphabet
	"""
	global is_data_input            # declare global variable
	read_dictionary()               # read the dictionary into dic_list
	for i in range(4):              # we need to input four lines of data, so need a for loop for four times
		"""
		check if the input format is correct or not
		if format is correct, keep input.
		if format is wrong, stop the algorithm
		"""
		if is_data_input:
			s = input(str(i+1) + ' row of letter : ')  # input data
			s = s.lower()                              # keep the data we input as lower alphabet
			s = s.split()                              # separate the data we input
			if len(s) != 4:                            # if the data length is not equal 4
				print('Illegal input!!!')                # it is a illegal iuput
				is_data_input = False                    # stop input procedure
				break                                    # stop loop
			for j in range(4):                         # check every length of alphabet is equal 1
				if len(s[j]) != 1:                       # if not equal 1
					print('Illegal input!!!')            # it is a illegal input
					is_data_input = False                # stop input procedure
					break                                # stop loop
				else:                                  # if all the length of alphabet is equal 1
					if j == 3:                           # when it is the last alphabet in data
						data_list.append(s)              # add it into data list
	boggle()                                           # start boggle


def boggle():
	"""
	This algorithm is to find all the possible word on every alphabet we input
	"""
	for r in range(len(data_list)):          # for loop to read every alphabet we input
		for c in range(len(data_list[1])):   # for loop to read every alphabet we input
			word_location.append((r,c))      # add the first word index into word location list because pass only once
			boggle_helper(r, c, '')          # create a helper function to find boggle
			word_location.pop()              # delete the first word index from word location list
	print(f'There are {total} words in total')     # print the result


def boggle_helper(r, c, get_word):
	"""
	:param r: the index of word lphabet, for rows
	:param c: the index of word alphabet, for columns
	:param get_word: the word we found
	"""
	global total, word_location                               # declare global variable
	if get_word in dic_list:                                  # for every word in the dict_list
		# for length of word is larger than four and not in find_word list
		if len(get_word) >= 4 and get_word not in find_word:
			print('Found "'+get_word+'"')                     # print the result
			find_word.append(get_word)                        # add the word we found in find_word list
			total += 1                                        # total plus one
	for i in range(-1, 2):                                    # for loop to formulate candidate area
		for j in range(-1, 2):                                # for loop to formulate candidate area
			if 0 <= r+i <= 3 and 0 <= c+j <= 3:               # if condition to check where is our candidate area
				candi = (r+i, c+j)
				# if candi is not in word_location, mean we still not use the word, so we can use it
				if candi not in word_location:
					word_location.append(candi)               # add the candi into word_location list
					# choose
					element = data_list[r + i][c + j]         # assign alphabet into element
					get_word_storage = get_word               # storage the word we found now
					get_word += element                       # add the element(alphabet) into get_word
					# explore
					if has_prefix(get_word):                  # if there is word start with "get_word"
						boggle_helper(r+i, c+j, get_word)       # keep explore with the alphabet
					# un-choose
					get_word = get_word_storage               # assign the word on the previous stack frame back
					word_location.pop()                       # delete the index in the index_list


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as file:  # read the file
		for word in file:          # for every word in the file
			word = word.strip()    # erase the spacing
			dic_list.append(word)  # add it into list


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for ele in dic_list:           # for every word in the dictionary
		ele.startswith(sub_s)      # if element is start with 'sub_s'
		if ele.startswith(sub_s):  # if is start with ''sub_s'
			return True            # return True


if __name__ == '__main__':
	main()
