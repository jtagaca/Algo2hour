
# O(N* 2^n) because for each element we make two more that is the len of the subset.

def powerset(array):
    # Write your code here.

    # if i== to the len of array then we append it.
    # but the array should be unique
    # 2^n
    subset = [[]]
    for element in array:
        # til but not including len(subset)
        for i in range(len(subset)):
            currentsubset = subset[i]
            # appending a new array to the subset.
            # we mutate the current subset and make a new array and append it to the subset.
            subset.append(currentsubset+[element])

    return subset
