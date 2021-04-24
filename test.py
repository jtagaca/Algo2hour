#T=O(n(logn)+m(logm)) S= O(1) since the array does not grow but remains the same
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
	oput=[]
	arrayOne.sort()
	arrayTwo.sort()
	
	p1=0
	p2=0
	prevtab=float("inf")
	currentabs=float("inf")
	while p1 <len(arrayOne) and p2 <len(arrayTwo):
	
	    currentabs=abs(arrayOne[p1]-arrayTwo[p2])
	
	
	    if prevtab > currentabs:
	        prevtab=currentabs
	        oput=[arrayOne[p1], arrayTwo[p2]]
	
	    if currentabs== 0:
	        return [arrayOne[p1], arrayTwo[p2]]
	    else:
	        if arrayOne[p1]> arrayTwo[p2]:
	            p2+=1
	        elif arrayOne[p1]<arrayTwo[p2]:
	            p1+=1
	
	return oput