"""
File: rocket.py
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


SIZE = 4


def main():
	"""
	build the rocket using head, belt, upper and lower part.
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def lower():
	"""
	this part is to build the lower part of racket
	"""
	for i in range(SIZE):
		print('|', end="")
		for j in range(i):              # this part is for the dot on th left hand side
			print('·', end="")
		for k in range(SIZE-i):         # this part is for the slash on th left hand side
			if i % 2 == 0:              # consider index system of i and k
				if (i+k) % 2 == 0:      # use the reminder of (i+k) divided 2 to decide print \ or / first
					print('\\', end="")
				else:
					print('/', end="")
			else:
				if (i+k) % 2 == 0:
					print('/', end="")
				else:
					print('\\', end="")
		for l in range(SIZE-i):         # this part is for the slash on th right hand side
			if SIZE % 2 == 0:           # consider the size of rocket and the reminder of divided by 2
				if (i+l) % 2 == 0:      # use the reminder of (i+l) divided 2 to decide print \ or / first
					print('\\', end="")
				else:
					print('/', end="")
			else:                       # SIZE also influence to print \ or / first
				if (i+l) % 2 == 0:      # use the reminder of (i+l) divided 2 to decide print \ or / first
					print('/', end="")
				else:
					print('\\', end="")
		for m in range(i):               # this part is for the dot on th right hand side
			print('·', end="")
		print('|')


def upper():
	"""
	this part is to build the upper part of racket
	"""
	for i in range(SIZE):
		print('|', end="")
		for j in range(SIZE):                 # this part is for the slash and dot on th left hand side
			if (i+j) >= (SIZE-1):             # use the index system to check print dot or slash
				if SIZE % 2 == 1:             # use the reminder to check print \ or / first
					if (i+j) % 2 == 1:        # SIZE and (i+j) will affect print \ or / first
						print('\\', end="")
					else:
						print('/', end="")
				else:
					if (i+j) % 2 == 1:
						print('/', end="")
					else:
						print('\\', end="")
			else:
				print('·', end="")
		for k in range(i+1):                   # this part is for the slash on th right hand side
			if (i+k) % 2 == 0:                 # use the reminder to check print \ or / first
				print('\\', end="")
			else:
				print('/', end="")
		for l in range((SIZE-1)-i):            # this part is for the dot on the right hand side
			print('·', end="")
		print('|')


def belt():
	"""
	to build the connect part between head and upper part or lower part
	"""
	print('+',end ="")
	for i in range(2*SIZE):
		print('=',end="")
	print('+')


def head():
	"""
	to build the head part
	"""
	for i in range(SIZE):
		print(' ', end="")
		for j in range(SIZE):       # form the left part of head
			if (i+j) >= (SIZE-1):
				print('/', end="")
			else:
				print(' ', end="")
		for K in range(i+1):        # form the right part of head
			print('\\', end="")
		print('')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()