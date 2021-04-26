#o(n) at T and for S it is O(1)
def isMonotonic(array):
	
    # Write your code here.
	# we wanna check if one of the trned is good and if not then we are not monotonic 
	# a monotonic array is where it is either decreasing or increasing.
	#return false when it is not 
	areWeNotDec=True
	areWeNotIncr=True
	for i in range(1,len(array)):
	
		if array[i]>array[i-1]:
			areWeNotDec=False
		elif array[i]<array[i-1]:
			areWeNotIncr=False
			
	#key here is that once it is false there is no turning it to a true and the return statement below it checks to see if
	# one of the boolean value is at least true this will only happen if wewere either increasing of decreasing.
	return areWeNotIncr or areWeNotDec
		

