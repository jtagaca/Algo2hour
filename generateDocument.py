def generateDocument(characters, document):
    # Write your code here.
	#time complexity is O(n+m) and space is O(c) where n is the length of chars and m is the len of document
	#c is the number of unique chars in the array
	h = {"": float("inf")}
	for letter in characters:
		if letter in h:
			h[letter] += 1
		else:
			h[letter] = 1
	for letter in document:
		if letter in h and h[letter] > 0:
			h[letter] -= 1
		else:
			return False
    return True
