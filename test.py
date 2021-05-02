def spiralTraverse(array):
    # Write your code here
    startrow = 0
    endrow = len(array)-1
    startcol = 0
    endcol = len(array[0])-1
    spiralarray = []

    while startrow <= endrow:
		spiralarray.append(array[startrow][startcol])
		if startcol == endcol:
            startrow += 1
        else:
            startcol += 1
    return spiralarray 


	
array = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]

# spiralarray.append(array[startrow][startcol])

# print(len(array[0]))
# print(array[1][2])
v = spiralTraverse(array)
print(v)
