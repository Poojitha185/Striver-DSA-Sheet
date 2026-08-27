#Time Complexity: O(n), where n is the number of nodes in the binary tree. Each node is visited exactly once.
#Space Complexity: O(h), where h is the height of the binary tree. This is the space required for the stack to store the nodes during traversal.
#Initialize an empty stack.
#Enter a loop that continues as long as there are nodes in the stack or the current node is not null. If the current node is not null, push it onto the stack and move to its left child. Continue this process until a node with no left child is reached. Once a null node is encountered, pop the top node from the stack, process it (e.g., add its value to the result array), and move to its right child.
#Repeat this process of pushing and popping nodes, alternating between moving left and right, until the stack is empty and the current node is null.


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
def itertaive_inorder_traversal(node):
    stack=[]
    inorder=[]
    while True:
        if node!=None:                 #while checking we check only existence of node irrespective of its value
            stack.append(node)         #node is a object here and we are pushing a object inside a stack
            node=node.left             #Go to its left child
        else:
            if not stack:
                break
            node = stack.pop()
            inorder.append(node.data)  #getting its value to store in inorder
            node=node.right            #Go to its right child
    return inorder

'''while stack or node is not None:
    if node is not None:
        stack.append(node)
        node = node.left
    else:
        node = stack.pop()
        inorder.append(node.data)
        node = node.right
    return inordern'''

root=create_tree()
result = itertaive_inorder_traversal(root)
print("Inorder Traversal:", result)