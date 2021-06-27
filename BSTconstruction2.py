# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # O(logn) because we keep having the bst time O(1) for space because were not using extra frames to do it
    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
		currentNode = self
		while True:
			if value < currentNode.value:
				if currentNode.left is None:
					currentNode.left = BST(value)
					break
				else:
					# we keep traversing if we cannot insert the node
					currentNode = currentNode.left
            # because if the value is the same or more than the passed down value then we do this
			else:
				if currentNode.right is None:
					currentNode.right = BST(value)
					break;
				# we keep traversing if we cannot insert the node
				else:
					currentNode = currentNode.right

        return self

    def contains(self, value):
        # Write your code here.
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False

    def remove(self, value, parentNode=0):
        # Write your code here.
        # Do not edit the return statement of this method.
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                # we are saving the current node to be the parent then we are traversing to the left
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                 # we are saving the current node to be the parent then we are traversing to the right
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                
                # We are now removing
                # edge case for removing a node that has two children 
                if currentNode.left is not None: and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()

                elif parentNode is None:


# edge case for removing a node in between that has a parent and a child ↓
                elif parentNode.left == currentNode.left:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode.right:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                



        return self
