def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
	#wee need to check who has the highest number 
	#(nlogn) because we sorted O(1)
	#jst to keep track of who should be the first 
	redShirtHeights.sort(reverse=True)
	blueShirtHeights.sort(reverse=True)
	
	# way to keep track of who is the first 
	whoShouldbefirst="red" if redShirtHeights[0]> blueShirtHeights[0] else "blue"
	for i in range(len(redShirtHeights)):
		redshirt=redShirtHeights[i]
		blueshirt=blueShirtHeights[i]
		if whoShouldbefirst=="red":
			# if any of the redshirt(a value in redshirts) is less than because redshirts should be taller than the blue then 
			# it will return false same applies for the else 
			if redshirt<=blueshirt:
				return False
			
		else:
			if blueshirt<=redshirt:
				return False
	return True
			
			