#time O(nlog) space is O(n)
def sortedSquaredArray(array):
    # Write your code here.
	sqarr=[]
	for num in array:
		sqnum=num*num
		sqarr.insert(-1,sqnum)
		sqarr.sort()
    return sqarr



#O(n) S O(n)

def sortedSquaredArray(array):
    # Write your code here.
	sortsquared=[0 for _ in array]
	left = 0
	right= len(array)-1

	for i in reversed(range(len(array))):
		smallvalue=array[left]
		largervalue=array[right]
		if abs(smallvalue)>abs(largervalue):
			sortsquared[i]=smallvalue*smallvalue
			left=left+1





		else:
			sortsquared[i]=largervalue* largervalue
			right=right-1

    return sortsquared
