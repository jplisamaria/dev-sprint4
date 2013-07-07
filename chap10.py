from bisect import bisect_left

# *******************
# ** Exercise 10.7 **
# *******************
# Anagrams
# -------------------------------
def is_anagram (word1, word2):
	'''Takes 2 words as arguments and returns True if they
	are anagrams of each other.'''
	if len(word1) != len(word2):
		return False
	for i in range (0,len(word1)):
		if word1[i] != word2[-1*(i+1)]:
			return False
	return True

def print_results(word1, word2):
	if is_anagram(word1, word2):
		print word1, "and", word2, "are anagrams"
	else:
		print word1, "and", word2, "are not anagrams"

word1 = 'noon' 
word2 = 'noon'
word3 = 'that'
word4 = 'hat'
word5 = 'abcdefg'
word6 = 'gfeccab'

print
print "Anagrams"
print "--------"
print_results(word1,word2)
print_results(word3,word4)
print_results(word5,word6)
print
print



# *******************
# ** Exercise 10.3 **
# *******************
# Interlocking Words
# -------------------------------

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Functions related to interlocking words +++++++++++++++++++
def is_interlockable (word1, word2):
	'''Takes two words and checks if they are interlockable. 
	Returns a list with the following elements:
	[0] is False if words are more than 1 character length apart
		(i.e. are not interlockable).
	[1] is True if the words are the same length
	[2] is the longer word (or the first word if they are the 
		same length)
	[3] if the shorther word (or the second word if they are 
		both the same length)''' 
	if len(word1) == len(word2):
		return [True, True, word1, word2]
	elif len(word1) == 1 + len(word2):
		return [True, False, word1, word2]
	elif len(word2) == 1 + len (word1):
		return [True, False, word2, word1]
	return [False, None, None, None]

def mesh(same_length,word1, word2):
	'''Takes three arguments, word1 and word2 (strings), and 
	same_length (a boolean which should be true if both
	words are the same length.  Returns the word that is
	the mesh of the two string arguments)'''
	new_word = ''
	for i in range (0,len(word1)-1):
		new_word = new_word + word1[i]+ word2[i]
	new_word = new_word + word1[-1]
	if same_length == True:
		new_word = new_word + word2[-1]
	return new_word

def perform_interlock(word1, word2):
	'''Takes two words, checks to see if they are 
	interlockable, and meshes them if they are. 
	Returns a list of two meshed words, each starting
	with a different argument.  An return item may be None, 
	if the words are not interlockable or meshable.'''
	locktest = is_interlockable(word1,word2)
	lockable = locktest[0]
	same_length = locktest [1]
	bigger_word = locktest[2]
	smaller_word = locktest[3]
	if lockable == False:
		return [None, None]
	elif same_length == True:
		return [mesh(same_length,bigger_word,smaller_word), 
				mesh(same_length, smaller_word, bigger_word)]
	else:
		return [mesh(same_length, bigger_word, smaller_word), 
				None]

def find_baseword_interlocks(word_list, baseword):
	'''Finds all interlacable words for a given baseword.'''
	baseword_interlocks = []
	for tempword in wordlist:
		result = perform_interlock(baseword, tempword)
		#print "baseword", baseword, "tempword", tempword,
		#print "result", result
		if result[0]!= None:
			if in_bisect(wordlist, result[0]):
				print '++++++', result[0]
				baseword_interlocks.extend([result[0]])
			if result[1] != None:
				if in_bisect(wordlist, result[1]):
					print '******', result[1]
					baseword_interlocks.extend([result[1]])
	return baseword_interlocks				
# End Functions related to interlocking words ++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Functions related to getting and searching for words, ++++++
#                             Taken from 'Think Python' ++++++ 
def make_word_list(fin):
	""" Taken from 'Think Python.' Reads lines from a file 
	and builds a list using append."""
	word_list = []
	for line in fin:
		word = line.strip()
		word_list.append(word)
	return word_list

def in_bisect(word_list, word):
	"""Taken from 'Think Python.'Checks whether a word is 
	in a list using bisection search.
	Precondition: the words in the list are sorted
	word_list: list of strings
	word: string"""
	i = bisect_left(word_list, word)
	if i != len(word_list) and word_list[i] == word:
		return True
	else:
		return False
# End Functions related to getting and searching for words +++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++













# Main Program
# ------------

fin = open('testwords.txt')
wordlist = make_word_list(fin)
basewords = wordlist
interlocked_words = []

print "Interlocked Words"
print "-----------------"

## This search process has problems because it skips certain words.
while (basewords != []):  
	baseword = basewords[0]
	#print baseword
	baseword_list = find_baseword_interlocks(wordlist, baseword)
	interlocked_words.extend(baseword_list)
	del basewords[0]

## This search product is very redundant and produces duplicates.
#for baseword in wordlist:
	#baseword_list = find_baseword_interlocks(wordlist, baseword)
	#interlocked_words.extend(baseword_list)

for i in range(len(interlocked_words)):
	print interlocked_words[i]
