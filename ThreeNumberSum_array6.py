#T= O(n) S= O(n) because we used an array that grew the same way as the input
def threeNumberSum(array, targetSum):
    # Write your code here.
	array.sort()
	oput=[]

	currentSum=0
	
	for i in range(len(array)-2): # so that it does not go out of bounds the last one is savaing for the right pointer while the other one is for the left pointer since it is +1
		currentnumber= i
		left= currentnumber+1
		right=len(array)-1
		
		while left < right:
			currentSum=array[currentnumber]+ array[left]+array[right]
			if targetSum == currentSum:
				oput.append([array[currentnumber], array[left], array[right]])
				right-=1 #but you can just remove right or left increment in this if statement since the other elif will still check it next run
				left+=1
    		elif currentSum>targetSum:
				right-=1
			elif currentSum<targetSum:
				left+=1
	return oput




