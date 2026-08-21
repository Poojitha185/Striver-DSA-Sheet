

#representation of binary tree in python
class node:                   #creates a blueprint/template for a tree node.
    def __init__(self,data):  #__init__ is a special Python method that runs automatically when you create an object.You could technically use another method, but then you'd have to call it yourself. __init__ is convenient because Python calls it automatically when the object is created.
        self.data=data        #self means the current Node object.
        self.left=None        #None simply means there is currently no child there.In Python, None is basically the equivalent of null in languages like C, C++, Java, and JavaScript.
        self.right=None
def pre_in_post(root):
    preorder=[]
    inorder=[]
    postorder=[]
    stack=[(root,1)]
    if root is None:
        return []
    while stack:
        node,state=stack.pop()
        if state==1:
            preorder.append(node.data)
            stack.append((node,2))
            if node.left:
                stack.append((node.left,1))
        elif state==2:
            inorder.append(node.data)
            stack.append((node,3))
            if node.right:
                stack.append((node.right,1))
        else:
            postorder.append(node.data)
    return [preorder,inorder,postorder]

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

# Create the tree
root = create_tree()
# Find traversals
result = pre_in_post(root)
print("Preorder:", result[0])
print("Inorder:", result[1])
print("Postorder:", result[2])
