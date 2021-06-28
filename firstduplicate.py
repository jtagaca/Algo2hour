def firstDuplicateValue(array):
    # Write your code here.
    # Program will run O(n)for time  and O(1) for space
    # we are using the value as a way to map the values to a different index and convert 
    # it to a negative value once they are found because an array[2] that converts it to -8
    # so when we find another 2 then we see that the value that it is mapped to is already 
    # negative then that is when we found a deplicate 
    for i in range(len(array)):
        absoluteval = abs(array[i])
        if array[absoluteval-1] < 0:
            return absoluteval
        array[absoluteval-1] *= -1
    return -1


# make sure to tell the brute force first then optimize as you go