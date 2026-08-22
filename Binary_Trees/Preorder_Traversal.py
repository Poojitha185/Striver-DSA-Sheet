#Time Complexity: O(N), we process each node once for traversal.
#Space Complexity: O(N), extra space used for storing preorder traversal and recursive stack.
#Preorder traversal is one of the depth-first traversal methods used to explore nodes in a binary tree. The algorithm first visits the root node then in the preorder traversal, we visit (ie. add to the array) the current node by accessing its value then we recursively traverse the left subtree in the same manner. We repeat these steps for the left subtree then when we return to the current node, we recursively travel to the right subtree in a preorder manner as well.The sequence of steps in preorder traversal follows: Root, Left, Right.

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
def preorder_traversal(node):
    if node is None:                  #After creating the tree, a missing child is None, not -1.
        return
    print(node.data)
    preorder_traversal(node.left)
    preorder_traversal(node.right)

# Create the tree
root = create_tree()
# Find traversals
preorder_traversal(root)
