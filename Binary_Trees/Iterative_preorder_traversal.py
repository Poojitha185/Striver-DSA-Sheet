#Time Complexity: O(N), where N is the number of nodes in the binary tree. Each node is visited once during the traversal.

#Space Complexity: O(H), where H is the height of the binary tree. The space is used by the stack to store nodes during traversal.

#iterative approach using stack to traverse the binary tree in preorder (root, left, right) manner. The algorithm uses a stack to keep track of nodes to be processed. It starts by pushing the root node onto the stack. Then, it enters a loop that continues until the stack is empty. In each iteration, it pops a node from the stack, processes it (adds its value to the result), and pushes its right child followed by its left child onto the stack (if they exist). This ensures that the left child is processed before the right child, maintaining the preorder traversal order.

class node:                   #creates a blueprint/template for a tree node.
    def __init__(self,data):  #__init__ is a special Python method that runs automatically when you create an object.You could technically use another method, but then you'd have to call it yourself. __init__ is convenient because Python calls it automatically when the object is created.
        self.data=data        #self means the current Node object.
        self.left=None        #None simply means there is currently no child there.In Python, None is basically the equivalent of null in languages like C, C++, Java, and JavaScript.
        self.right=None
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

def preorderTraversal(root):
    preorder = []  # List to store the preorder traversal result
    # If the root is null, return an empty traversal result
    if root is None:
        return preorder
    stack = [root]  # Stack to store nodes during traversal
    while stack:
        node = stack.pop()  # Get the current node from the top of the stack
        preorder.append(node.data)  # Add the node's value to the preorder result
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return preorder

 # Getting the preorder traversal
root=create_tree()
result = preorderTraversal(root)

# Displaying the preorder traversal result
print("Preorder Traversal:", result)