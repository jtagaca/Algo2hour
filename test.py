def moveElementToEnd(array, toMove):
    # Write your code here
	left= 0
	right= len(array)-1
	while  left <right  or left==right :
		if array[left]==toMove and array[right]==toMove:
			array[left],array[right]=array[right], array[left]
			left+=1
			right-=1
		elif left < right:
			if array[left]!=toMove:
				left+=1
			if array[right]==toMove:
				right-=1
			
	return array



array=[2, 1, 2, 2, 2, 3, 4, 2]
toMove=2

moveElementToEnd(array, toMove)