def isValidSubsequence(array, sequence):
    # Write your code here.
	current=0
	for num in array:
		if sequence[current]==num:
			current=current +1
		if current==len(sequence):
			return True
	return False
			
