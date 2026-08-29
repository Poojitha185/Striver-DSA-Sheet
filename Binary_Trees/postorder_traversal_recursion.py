#Time Complexity: O(N), we process each node once in traversal.
#Space Complexity: O(N), extra space used for storing post order traversal and recursion stack space.
#Postorder traversal, another depth-first method in tree exploration, follows a sequence where the algorithm first explores the left subtree, then the right subtree, and finally visits the root node. In postorder traversal, we visit (or add to the array) the current node after traversing both its left and right subtrees.The sequence of steps in postorder traversal follows: Left, Right, Root.
#Start at the root of the binary tree.First, recursively traverse the entire left subtree.Then, recursively traverse the entire right subtree.
#Finally, process (visit) the current node.
#recursion approach

class node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
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


