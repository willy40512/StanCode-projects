"""
File: boggle.py
Name: Willie Li
----------------------------------------
The file is inspired by the boggle game, the user will obtain
the possible combination of the word under the boggle rule.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global variable
dictionary_list = []

def main():
	"""
	The user will require to enter 4 row of alphabet,
	and the program will search the possible word with
	the role of boggle.
	"""
	lst = []
	read_dictionary()
	while True:
		row1 = input("1 row of letters: ")
		row1.lower()
		if len(row1) > 7 or len(row1) <= 4:
			print("Illegal input")
			break
		lst.append(row1.split())
		row2 = input("2 row of letters: ")
		row2.lower()
		if len(row2) > 7 or len(row2) <= 4:
			print("Illegal input")
			break
		lst.append(row2.split())
		row3 = input("3 row of letters: ")
		row3.lower()
		if len(row3) > 7 or len(row3) <= 4:
			print("Illegal input")
			break
		lst.append(row3.split())
		row4 = input("4 row of letters: ")
		row4.lower()
		if len(row4) > 7 or len(row4) <= 4:
			print("Illegal input")
			break
		lst.append(row4.split())
		find_word(lst)
		break

def helper(current_string, possible_word, ch_index, lst):
	"""
	:param current_string: string, connect the single word
	:param possible_word: list, contain the possible combination
	:param ch_index: int, index for the word
	:param lst: list, contain the word entered by users, like [[first row],[second row],[third row],[fourth row]]
	:return: list of possible word
	"""
	# Base-case: the vocabulary over 4 word
	# and the vocabulary that can be search in dictionary did not exist in the possible list
	if len(current_string) >= len(lst) and current_string in dictionary_list and current_string not in possible_word:
		possible_word.append(current_string)
		print(f'Found "{current_string}"')
		helper(current_string, possible_word, ch_index, lst)
	# Recursive-Case
	else:
		#  loop for every row
		for i in range(len(lst)):
			# loop for the word in every row
			for j in range(len(lst[i])):
				ch = lst[i][j]
				# using the i and j for noting the precise position, like [0,0]
				ch_index.append([i, j])
				# the latest position of new word
				new_data_index = len(ch_index)-1
				# when the index only have first word and initial [0,0], initial [0,0] will be change for next new word
				if len(ch_index) <= 2:
					ch_index[0][0] = i
					ch_index[0][1] = j
				# first two line is to calculate for the distance of the index to fit the rule of boggle
				# third line to examine whether the word have been appeared
				if ((ch_index[new_data_index][0] - ch_index[new_data_index-1][0])**2)**0.5 <= 1 \
					and ((ch_index[new_data_index][1] - ch_index[new_data_index-1][1])**2)**0.5 <= 1\
					and ch not in current_string:
					current_string += ch
					if has_prefix(current_string):
						helper(current_string, possible_word, ch_index, lst)
					# un-choose the word
					current_string = current_string[:len(current_string) - 1]
				# first two line is to calculate for the distance of the index to fit the rule of boggle
				# third line to examine whether the word have been appeared
				elif ((ch_index[new_data_index][0] - ch_index[new_data_index-1][0])**2)**0.5 <= 1 \
					and ((ch_index[new_data_index][1] - ch_index[new_data_index-1][1])**2)**0.5 <= 1\
					and ch in current_string:
					# to examine whether the same word have repeat index
					if no_repeat_index(i, j, ch_index):
						current_string += ch
						if has_prefix(current_string):
							helper(current_string, possible_word, ch_index, lst)
						# un-choose the word
						current_string = current_string[:len(current_string) - 1]
				# eliminate the index of unnecessary word
				ch_index.pop()


def no_repeat_index(i, j, ch_index):
	"""
	:param i: int, the index of new alphabet
	:param j: int, the index of new alphabet
	:param ch_index: list, contain the whole index for the current string
	:return: boolean
	"""
	for ele in ch_index[1:-1]:
		if ele[0] == i and ele[1] == j:
			return False
	return True

def find_word(lst):
	s = ''
	possible_word = []
	# the initial index of the list
	ch_index = [[0, 0]]
	helper(s, possible_word, ch_index, lst)
	print(f'There are {len(possible_word)} words in total')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			# eliminate the new line(/n)
			dictionary_list.append(line[0:len(line) - 1])


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary_list:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
