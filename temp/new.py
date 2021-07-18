def removeIslands(matrix):
    # Write your code here.
	visited = [[False for col in matrix[0]] for row in matrix]
	for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                continue
			if matrix[row][col] == True:
				continue
			visited[row][col] = True
            if isPartofBounds(row, col, matrix, visited) == False:
                matrix[row][col] = 0

    return matrix


def isPartofBounds(row, col, matrix,visited):
    stack = [[row, col]]
    while len(stack) > 0:
        current = stack.pop()
        currentRow, currentCol = current
		visited[currentRow][currentCol]=True
        if currentRow == 0 or currentRow == len(matrix)-1 or currentCol == 0 or currentCol == len(matrix[0])-1:
            return True
        if matrix[currentRow-1][currentCol] == 1 and visited[currentRow-1][currentCol]==False:
            stack.append([currentRow-1, currentCol])
        if matrix[currentRow+1][currentCol] == 1 and visited[currentRow+1][currentCol]==False:
            stack.append([currentRow+1, currentCol])
        if matrix[currentRow][currentCol-1] == 1 and visited[currentRow][currentCol-1]==False:
            stack.append([currentRow, currentCol-1])
        if matrix[currentRow][currentCol+1] == 1 and visited[currentRow][currentCol+1]:
            stack.append([currentRow, currentCol+1])
    return False
