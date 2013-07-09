#Dev-Sprint4, Ch. 10
#Name: Lisa-Maria Mehta

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


# Main Program
# ------------
word1, word2, word3 = 'noon', 'noon', 'that' 
word4, word5, word6 = 'hat', 'abcdefg', 'gfeccab'
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
# Functions related to uninterlocking words +++++++++++++++++++

def unmesh_word(word):
	'''Takes a word (longer than one character), and returns the
	"uninterlocked" components.  Returns a list with two strings'''
	longstr = ''
	shortstr = ''
	l = len(word)
	l_long = l/2 + l%2 +1
	l_short = l/2 + 1

	for i in range(0,l_long-1):
		longstr += word[2*i]
	for i in range(0, l_short-1):
		shortstr += word[2*i+1]
	return [longstr, shortstr] 

def are_they_words(wordlist, str1, str2):
	'''Takes 2 strings, and returns True if they are both words.'''
	if in_bisect(wordlist, str1):
		if in_bisect(wordlist, str2):
			return True
	return False

# End Functions related to uninterlocking words ++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


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

def print_dict(k):
	for c in k:
		print c, k[c]


# Main Program
# ------------
textfile = 'words.txt'
fin = open(textfile)
wordlist = make_word_list(fin)
interlocked_words = dict()
count = 0

print "Interlocked Words"
print "-----------------"
for word in wordlist:
	halfwords = unmesh_word(word)
	if are_they_words(wordlist, halfwords[0], halfwords[1]):
		interlocked_words[word] = [halfwords[0], halfwords[1]]
for key in sorted(interlocked_words.iterkeys()):
	print "%s:     %s" % (key, interlocked_words[key])
#print_dict(interlocked_words)
print len(interlocked_words), "interocked words"