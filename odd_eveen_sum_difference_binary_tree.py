from collections import deque

# Define the TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def differenceOddEvenLevel(root: TreeNode) -> int:
    if not root:
        return 0

    # Initialize sums for odd and even levels
    odd_sum = 0
    even_sum = 0

    # Initialize the queue for level order traversal
    queue = deque([(root, 1)])  # Each element is a tuple (node, level)

    while queue:
        node, level = queue.popleft()

        # Add the node's value to the corresponding level sum
        if level % 2 == 1:
            odd_sum += node.val
        else:
            even_sum += node.val

        # Add the child nodes to the queue with the incremented level
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    # Return the difference between odd level sum and even level sum
    return odd_sum - even_sum

# Example usage
# Construct the binary tree
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6
# Example tree structure
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(differenceOddEvenLevel(root))  # Output: -6
