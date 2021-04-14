#AVG O(logn) time and space O(1)
#worst o(n) and space O(1)
def findClosestValueInBst(tree, target):
    # Write your code here.


    return helper(tree, target, tree.value)

def helper(tree, target, closest):
	current=tree
	while current is not None:
		if abs(closest-target)>abs(target-current.value):
			closest=current.value
		if target< current.value:
			current=current.left
		elif target> current.value:
			current=current.right
			
		else:
			break
	return closest
	


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
