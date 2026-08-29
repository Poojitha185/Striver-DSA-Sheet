#Time Complexity: O(N), we process each node once in traversal.
#Space Complexity: O(N), extra space used for storing post order traversal and recursion stack space.
class node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def create_tree():
    data = int(input("Enter data (-1 for no node): "))
    if data == -1:
        return None
    root = node(data)
    print("Enter left child of", data)
    root.left = create_tree()
    print("Enter right child of", data)
    root.right = create_tree()
    return root
def postorderTraversal(root, result):
        # Base case: if node is None
        if not root:
            return
        # Traverse left subtree
        postorderTraversal(root.left, result)
        # Traverse right subtree
        postorderTraversal(root.right, result)
        # Add current node value
        result.append(root.val)

root=create_tree()
result = []
postorderTraversal(root, result)
print("Postorder Traversal:", result)


