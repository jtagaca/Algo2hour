# time complexity(O(n)) because we traverse everything and the space is O(d) where d is the height of the tree
# space the code has d function calls where d is the height of the tree
def nodeDepths(root, depth=0):

    # Write your code here.
    if root is None:
        return 0
    else:
        # we keep adding the depth of the tree from parent to child then if the node is none then we stop
        return depth+nodeDepths(root.left, depth+1)+nodeDepths(root.right, depth+1)


# This is the class of the input binary tree.
class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
