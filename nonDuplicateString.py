#O(n) time because 2O(n) is O(n) and this will run O(1) space mainly because we have a finite input
# where it is specified that the input will be lower case
def firstNonRepeatingCharacter(string):
    h = {}


for letter in string:
		# we are initializing the key if it's not available else we are adding 1
		h[letter] = h.get(letter, 0)+1
	for i, letter in enumerate(string):
		if letter in h and h[letter] ==1:
			return i

    return -1
