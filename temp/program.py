def powerset(array):
    # Write your code here.
	
	# if i== to the len of array then we append it. 
	# but the array should be unique
	# 2^n
	subset=[[]]
	for element in array:
		for i in range(len(subset)):
			currentsubset=subset[i]
			# appending a new array to the subset.
			subset.append(currentsubset+[element])
	
	
	return subset