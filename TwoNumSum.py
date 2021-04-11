#time is O(n) and space is O(n) because of the list 
def twoNumberSum(array, targetSum):
    # Write your code here
	dict={}
	for num in array:
		y=targetSum-num
		if y in dict:
			return[y, num]
		else:
			dict[num]=True
	return []

