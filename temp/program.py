def removeIslands(matrix):
    # Write your code here.

    isPart = [[False for col in matrix[0]] for row in matrix]
    for row in range(len(matrix)):
        # used for marking the location that are part of the 1 in the border side
        for col in range(len(matrix[0])):
            isBorderRow = row == 0 or row == len(matrix)-1
            isBorderCol = col == 0 or col == len(matrix[0])-1
            isBorder = isBorderRow or isBorderCol

            if not isBorder:
                continue
            # traversal in BFS for populating the isPart matrix
            if matrix[row][col] != 1:
                continue
            updateIsPart(row, col, matrix, isPart)
        # we want to update the values that do not have a T value in the isPart matrix
    for row in range(1, len(matrix)-1):
        for col in range(1, len(matrix[0])-1):
            if isPart[row][col] == True:
                continue
            if matrix[row][col] == 0:
                continue
            matrix[row][col] = 0
    return matrix

# here located where we update True


def updateIsPart(row, col, matrix, isPart):
    stack = [[row, col]]
    while len(stack) > 0:
        current = stack.pop()
        currentRow, currentCol = current

        if isPart[currentRow][currentCol] == True:
            continue
        # we are thinking that we will receive neighbors that are 1
        isPart[currentRow][currentCol] = True
        neighbors = getNeighbors(currentRow, currentCol, matrix)
        for neighbor in neighbors:
            tempRow, tempCol = neighbor
            if matrix[tempRow][tempCol] != 1:
                continue
            stack.append([tempRow, tempCol])


def getNeighbors(currentRow, currentCol, matrix):
    lenRow = len(matrix)-1
    lenCol = len(matrix[0])-1
    neighbor = []
    if currentRow-1 >= 0:
        neighbor.append([currentRow-1, currentCol])
    if currentRow+1 <= lenRow:
        neighbor.append([currentRow+1, currentCol])
    if currentCol-1 >= 0:
        neighbor.append([currentRow, currentCol-1])
    if currentCol+1 <= lenCol:
        neighbor.append([currentRow, currentCol+1])
    return neighbor
