def staircaseTraversal(height, maxSteps):
    # Write your code here.
    currentNum = 0
    listvar = [1]

    for currentHeight in range(1, height+1):
        startwin = currentHeight-maxSteps-1
        closewin = currentHeight-1
        if startwin >= 0:
            currentNum -= listvar[startwin]
        currentNum += listvar[closewin]
        listvar.append(currentNum)
