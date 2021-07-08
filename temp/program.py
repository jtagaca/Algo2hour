def staircaseTraversal(height, maxSteps):
    # Write your code here.
    # initialize result
    result = [0] * (height+1)
    # base cases
    result[0] = 1
    result[1] = 1

    for currentHeight in range(2, height+1):
        step = 1
        while step <= maxSteps and step <= height:
            result[currentHeight] += result[currentHeight-step]
            step += 1
        print(result)
    return result[height]
