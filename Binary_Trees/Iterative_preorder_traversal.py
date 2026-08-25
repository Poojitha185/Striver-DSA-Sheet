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