# TreeNode class for binary tree nodes
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # Recursive function to get left view
    def leftDFS(self, node, level, res):
        # Base case
        if not node:
            return

        # If we are visiting the level for the first time
        if len(res) == level:
            res.append(node.val)

        # Recurse to left child
        self.leftDFS(node.left, level + 1, res)

        # Recurse to right child
        self.leftDFS(node.right, level + 1, res)

    # Recursive function to get right view
    def rightDFS(self, node, level, res):
        if not node:
            return

        if len(res) == level:
            res.append(node.val)

        # Recurse to right child
        self.rightDFS(node.right, level + 1, res)

        # Recurse to left child
        self.rightDFS(node.left, level + 1, res)

    # Wrapper function for left view
    def leftView(self, root):
        res = []
        self.leftDFS(root, 0, res)
        return res

    # Wrapper function for right view
    def rightView(self, root):
        res = []
        self.rightDFS(root, 0, res)
        return res

# Driver code
if __name__ == "__main__":
    # Create the binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.right.right = TreeNode(5)
    root.left.right.right.right = TreeNode(6)

    sol = Solution()

    # Get left and right view
    left = sol.leftView(root)
    right = sol.rightView(root)

    # Print left view
    print("Left View:", left)

    # Print right view
    print("Right View:", right)
