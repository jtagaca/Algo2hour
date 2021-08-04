# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

		
class TreeInfo:
	def __init__(self, isBalanced, height):
		self.isBalanced=isBalanced
		self.height=height

		
def getTreeInfo(tree):
	
	if tree ==None:
		return TreeInfo(True, 0)
	l=getTreeInfo(tree.left)
	r=getTreeInfo(tree.right)
	isBalanced=l.isBalanced and r.isBalanced and abs(l.height-r.height)<=1
	height=1+max(l.height,r.height)
	
	return TreeInfo(isBalanced,height)
	
	
def heightBalancedBinaryTree(tree):
    # Write your code here.
    return getTreeInfo(tree).isBalanced
