#Time Complexity: O(N), where N is the number of nodes in the binary tree. Each node is visited exactly once during the traversal.
#Space Complexity: O(N), where N is the number of nodes in the binary tree. The space is used for the recursion stack during the traversal, which can go as deep as the height of the tree in the worst case (for a skewed tree). 
#Process Current Node: Once the left subtree is fully explored, the current node is processed (e.g., adding its value to an array or printing it).
#Traverse Right Subtree: After processing the current node, recursively explore the right subtree by invoking the inorder function on the right child of the current node.

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
def Inorder_traversal(node):
    if node is None:                  
        return
    
    Inorder_traversal(node.left)
    print(node.data)
    Inorder_traversal(node.right)

# Create the tree
root = create_tree()
# Find traversals
Inorder_traversal(root)
