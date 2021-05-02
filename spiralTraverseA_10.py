#time O(n) Sapce is O(n)
def spiralTraverse(array):
    # Write your code here
    startrow = 0
    endrow = len(array)-1
    startcol = 0
    endcol = len(array[0])-1
    spiralarray = []

    while startrow <= endrow and startcol <= endcol:
		for col in range(startcol, endcol+1):
            spiralarray.append(array[startrow][col])
        for row in range(startrow+1, endrow+1):
            spiralarray.append(array[row][endcol])
        for col in reversed(range(startcol, endcol)):
			if startrow==endrow:
				break
            spiralarray.append(array[endrow][col])
		for row in reversed(range(startrow+1, endrow)):
			if startcol==endcol:
				break
			spiralarray.append(array[row][startcol])
		
		endrow-=1
		endcol-=1
		startrow+=1
		startcol+=1
		
    return spiralarray