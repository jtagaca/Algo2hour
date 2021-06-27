def arrayOfProducts(array):
	# initialized 1 for the array products
    # O(n) for time complexity and O(n) for space complexity
    # for this problem explain the brute force which is the two nested for loop
	products = [1 for _ in range(len(array))]

    # products of the left is stored on an array then we multiply with the right array in order to
    # solve the problem for the array
    # we are storing first the array of products of the left of the index on the first for loop ↓
    leftproduct=1
    for i in range(len(array)):
        products[i] = leftproduct
        leftproduct *= array[i]
    rightproduct = 1
    # we are reversing it from the right of the array 
    for i in reversed(range(len(array))):
        # multiplying the product with the rightproduct which is the product to the right of i 
        products[i] *= rightproduct
        # updating the right product to be used in the next cycle
        rightproduct*=array[i]
    return products
