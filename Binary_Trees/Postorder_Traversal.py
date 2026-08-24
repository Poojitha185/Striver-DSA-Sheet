#Time Complexity: O(N), where N is the number of nodes in the binary tree. Each node is visited once during the traversal.
#Space Complexity: O(2N),The space is used by the 2 stacks to store nodes during traversal.
#Create two stacks: one for holding nodes and another for storing the final postorder traversal sequence. Initialize an array `postorder` to store the traversal sequence.
#Push the root node to the first stack.#Process the nodes until the first stack is empty:#Pop a node from the top of the first stack.
#Push this node onto the second stack.
#Push its left child (if it exists) onto the first stack.
#Push its right child (if it exists) onto the first stack.
#Once the first stack is empty, retrieve the nodes in the postorder sequence by popping nodes from the second stack one by one and store them in the postorder array.


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
def postorder_traversal(node):
    postorder=[]
    if node is None:
        return postorder
    st1=[]
    st2=[]
    st1.append(node)
    while st1:
        root=st1.pop()
        st2.append(root)
        if root.left is not None:
            st1.append(root.left)
        if root.right is not None:
            st1.append(root.right)
    while st2:
        postorder.append(st2.pop().data)
    return postorder

# Create the tree
root = create_tree()
# Find traversals
print(postorder_traversal(root))