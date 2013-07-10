#Dev-Sprint4, Ch. 10
#Name: Lisa-Maria Mehta

from bisect import bisect_left

# *******************
# ** Exercise 10.7 **
# *******************
# Anagrams
# --------
def is_anagram (word1, word2):
	'''
	Takes 2 words as arguments and returns True if they
	are anagrams of each other.
	Previously, is_anagram() erroneously checked for 
	palindromes. 
	Thanks to joytafty's code, I corrected mistake.
	'''
	if len(word1) != len(word2):
		return False
	list1 = list(word1)
	list2 = list(word2)
	list1.sort()
	list2.sort()
	if list1==list2:
		return True
	return False

def print_results(word1, word2):
	if is_anagram(word1, word2):
		print word1, "and", word2, "are anagrams"
	else:
		print word1, "and", word2, "are NOT anagrams"


# Main Program
# ------------
word1, word2 = 'nights', 'things' 
word3, word4 = 'nose', 'eons' 
word5, word6 = 'hat', 'cable'
word7, word8 = 'noose','nosee'
print
print "Anagrams"
print "--------"
print_results(word1,word2)
print_results(word3,word4)
print_results(word5,word6)
print_results(word7,word8)
print
print



# *******************
# ** Exercise 10.3 **
# *******************
# Interlocking Words
# ------------------

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Functions related to uninterlocking words ++++++++++++++++++++
#       Thank Dean's Piazza comment for better algorithm +++++++
#                                                  +++++++++++++
def unmesh_word(word):
	'''
	Takes a word (longer than one character), and returns the
	"uninterlocked" components.  Returns a list with two strings
	'''
	longstr = ''
	shortstr = ''
	l = len(word)
	l_long = l/2 + l%2 
	l_short = l/2 

	for i in range(0,l_long):
		longstr += word[2*i]
	for i in range(0, l_short):
		shortstr += word[2*i+1]
	return [longstr, shortstr] 

def are_they_words(wordlist, str1, str2):
	'''
	Takes 2 strings, and returns True if they are both words.
	'''
	if in_bisect(wordlist, str1):
		if in_bisect(wordlist, str2):
			return True
	return False

def make_dict(wordlist):
	interlocked_words = dict()
	count = 0
	for word in wordlist:
		if len(word)>1:
			halfwords = unmesh_word(word)
			if are_they_words(wordlist, halfwords[0], halfwords[1]):
				interlocked_words[word] = [halfwords[0], halfwords[1]]
	return interlocked_words
#                                                        +++++++
# End Functions related to uninterlocking words ++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Functions related to 3-way uninterlocking words ++++++++++++++
#                                                        +++++++
def un_mesh_3way(word):
	'''
	Takes a word (longer than two characters), and returns the
	"uninterlocked" components.  Returns a list with three strings.
	'''
	str1 = ''
	str2 = ''
	str3 = ''
	l = len(word)
	l_str1 = l/3
	l_str2 = l/3
	l_str3 = l/3
	if len(word)%3 != 0:
		l_str1 += 1
	if len(word)%3 == 2:
		l_str2 += 1

	for i in range(0,l_str1):
		str1 += word[3*i]
	for i in range(0, l_str2):
		str2 += word[3*i+1]
	for i in range(0, l_str3):
		str3 += word[3*i+2]
	return [str1,str2,str3] 


def are_they_words_3way(wordlist, str1, str2, str3):
	'''
	Takes 3 strings, and returns True if they are all words.
	'''
	if in_bisect(wordlist, str1):
		if in_bisect(wordlist, str2):
			if in_bisect(wordlist, str3):
				return True
	return False


def make_dict_3way(wordlist):
	interlocked_words = dict()
	for word in wordlist:
		if len(word)>2:
			triwords = un_mesh_3way(word)
			if are_they_words_3way(wordlist, 
							triwords[0], triwords[1], triwords[2]):
				interlocked_words[word] = [triwords[0], 
											triwords[1],
											triwords[2]]
	return interlocked_words
#                                                        +++++++
# End Functions related to uninterlocking words ++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Functions related to getting and searching for words, ++++++
#                             Taken from 'Think Python' ++++++ 
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
#                                                        +++++++		
# End Functions related to getting and searching for words +++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Main Program
# ------------
textfile = 'words.txt'
fin = open(textfile)
wordlist = make_word_list(fin)


print "Interlocked Words"
print "-----------------"
interlocked_words = make_dict(wordlist)
for key in sorted(interlocked_words.iterkeys()):
	print "%s:     %s" % (key, interlocked_words[key])
print len(interlocked_words), "interocked words"

print
print "Interlocked Words, 3-way"
print "------------------------"
interlocked_3way_words = make_dict_3way(wordlist)
for key in sorted(interlocked_3way_words.iterkeys()):
	print "%s:     %s" % (key, interlocked_3way_words[key])
print len(interlocked_3way_words), "3-way interocked words"
