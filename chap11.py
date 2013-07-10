#Dev-Sprint4, Ch. 11
#Name: Lisa-Maria Mehta

# ***********************************
# ** Exercise 11.9--has_duplicates **
# ***********************************
# 'Old' has_duplicates, from 10.8
# -------------------------------
def old_has_duplicates(lst):
	new_list=[]
	for element in lst:
		if element in new_list:
			return True
		new_list.append(element)	
	return False


# 'New' has_duplicates, from 11.9
# -------------------------------
def new_has_duplicates(lst):
	'''
	Had to look at solution, especially since 'set()' hasn't appeared
	in the text yet, but I looked it up on StackOverflow, and 
	think I understand it enough to use it.
	'''
	if len(lst)> len(set(lst)):
		return True
	return False
	### of course  "return len(set(t)) < len(t)" is more efficient
	### code writing, but not any faster processing time, right? 


# Main Program--Testing functions
# -------------------------------
yes=[1,2,2,5,7,7,9,]
no=['a','b','c']
print
print "has_duplicates, old"
print "------------------"
print old_has_duplicates(yes), "list 'yes' has duplicates"
print old_has_duplicates(no), "list 'no' has no duplicates"
print
print "has_duplicates, new, using dictionary"
print "-------------------------------------"
print new_has_duplicates(yes), "list 'yes' has duplicates"
print new_has_duplicates(no), "list 'no' has no duplicates"
print



# **************************************
# ** Exercise 11.10--Find ROT13 Pairs **
# **************************************
# Find all ROT13 pairs
# --------------------

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Functions related to getting and searching for words, ++++++
#                             Taken from 'Think Python' ++++++ 
#                                                    +++++++++ 
def make_word_list(fin):
	""" 
	Taken from 'Think Python.' Reads lines from a file 
	and builds a list using append.
	"""
	word_list = []
	for line in fin:
		word = line.strip()
		word_list.append(word)
	return word_list

def in_bisect(word_list, word):
	"""
	Taken from 'Think Python.'Checks whether a word is 
	in a list using bisection search.
	Precondition: the words in the list are sorted
	word_list: list of strings
	word: string
	"""
	i = bisect_left(word_list, word)
	if i != len(word_list) and word_list[i] == word:
		return True
	else:
		return False
#                                                    +++++++++ 
# End Functions related to getting and searching for words +++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Functions related to rotating words, +++++++++++++++++++++++
#                     from dev-sprint3 +++++++++++++++++++++++ 
#                                                    +++++++++       
def rotate_letter (letter, n):
	"""
	Takes a letter and an integer n as input, and returns letter
	n places away from original letter.
	From dev-sprint3.
	"""
	rotation_factor = n % 26
	new_letter_ord = ord(letter) + rotation_factor
	if letter.isupper():
		if new_letter_ord <=90:
			return chr(new_letter_ord)
		else:
			return chr(new_letter_ord - 26)
	elif letter.islower():
		if new_letter_ord <=122:
			return chr(new_letter_ord)
		else:
			return chr(new_letter_ord - 26)
	else:
		return letter

def rotate_word (word, n):
	"""
	Takes a word and an integer n as input.  Calls rotate_letter
	and returns a word with each letter n places away from
	original letters.
	From dev-sprint3
	"""
	new_word = ""
	for char in word:
		new_word = new_word +rotate_letter(char, n)
	return new_word

def rotate_all_words(wordlist):
	'''
	Rotates all words in wordlist.  Returns sorted list of 
	rotated strings.
	New to Dev-Sprint4.
	'''
	rotated_strings = []
	for i in range(0,len(wordlist)):
		rotated_word = rotate_word(wordlist[i],13)
		rotated_strings.append(rotated_word)
	rotated_strings.sort()
	return rotated_strings	
#                                                    +++++++++ 
# End Functions related to rotating words, +++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Functions related building and +++++++++++++++++++++++++++++
#                   printing dictionary ++++++++++++++++++++++ 
#                                                    +++++++++   
def find_ROT13_pairs(word_list):
	'''
	Given a wordlist, returns all ROT13 Pairs in a dictionary.
	'''
	rotated_wordlist = rotate_all_words(word_list)
	ROT13_pairs = dict()
	r = 0
	w = 0
	l = len(word_list)

	while (r < l) and (w < l): 
		rotated_word = rotated_wordlist[r]
		word = ''.join(word_list[w])
		if rotated_word < word:
			r +=1
		elif word < rotated_word:
			w += 1
		elif rotated_word == word:
			ROT13_pairs[rotated_word] = rotate_word(rotated_word,13)
			r += 1
			w += 1
	return ROT13_pairs		

def print_dict(k):
	'''Taken from Think Python.'''
	for c in k:
		print c, k[c]
#                                                    +++++++++
# End Functions related building and printing dictionary +++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Main Program
# ------------
textfile = 'shortlist.txt'
fin = open(textfile)
word_list = make_word_list(fin)

ROT13dict = find_ROT13_pairs(word_list)
print "ROT13 Pairs"
print "------------------"
print_dict(ROT13dict)