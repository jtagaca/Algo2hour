def searchForRange(array, target):
    # Write your code here.
	finalRange = [-1, -1]

	getFinalRange(array, target, 0, len(array)-1, finalRange, True)
	getFinalRange(array, target, 0, len(array)-1, finalRange, False)

    return finalRange

def getFinalRange(array,target,l ,r, finalRange, goLeft ):
	
	while l<=r:
		mid=(l+r)//2
		currentNum=array[mid]
		
		if target<currentNum:
			r=mid-1
		elif target> currentNum:
			l=mid+1
		else:  
			if goLeft:
				if mid==0 or array[mid-1]!=target:
					finalRange[0]=mid
					return
				else: 
					r=mid-1
			else:
				# code gets evaluated from left to right so since we got a true we just stoped 
				if mid==len(array)-1 or array[mid+1]!= target :
					finalRange[1]=mid
					return
				else:
					l=mid+1
	
