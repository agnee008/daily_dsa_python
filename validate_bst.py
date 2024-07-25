# Define the TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: TreeNode) -> bool:
    def validate(node, low=-float('inf'), high=float('inf')):
        # An empty tree is a valid BST
        if not node:
            return True
        
        # The current node's value must be within the range defined by low and high
        if node.val <= low or node.val >= high:
            return False
        
        # Recursively check the left subtree with updated high value
        # and the right subtree with updated low value
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)
    
    return validate(root)

# Example usage
# Construct the binary tree
#       2
#      / \
#     1   3
# Example tree structure
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(isValidBST(root))  # Output: True

# Example of an invalid BST
#       5
#      / \
#     1   4
#        / \
#       3   6
root_invalid = TreeNode(5)
root_invalid.left = TreeNode(1)
root_invalid.right = TreeNode(4)
root_invalid.right.left = TreeNode(3)
root_invalid.right.right = TreeNode(6)

print(isValidBST(root_invalid))  # Output: False
