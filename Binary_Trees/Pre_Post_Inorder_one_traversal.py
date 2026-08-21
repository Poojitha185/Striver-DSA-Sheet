#Time Complexity: O(3*N), we process each node thrice, once for every traversal.
#Space Complexity: O(4*N), extra space used for storing postorder, inorder, preorder traversal and stack.
#This approach traverses the binary tree in a single pass while computing the preorder, inorder and postorder traversals at the same time. A stack is used for state management. The stack keeps track of the traversal state for each node. 
#It stores nodes and their state information allowing the algorithm to resume traversal from intermediate points. For each node, it identifies its state i.e. if it's in the preorder state, it records the node's value and pushes the left child onto the stack.
#Moving to the inorder state, it records the node's value and pushes the right child onto the stack. Finally, in the post-order state, it stores the node's value and pops the node. As the algorithm executes over each node, it pushes each value in separate arrays for preorder, inorder and postorder traversals depending upon the current order and sequence. Hence, we are able to traverse the tree just once and get all three traversals from it.


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
        if state==1:                         #If the state is ‘1’ ie. preorder: store the node’s data in the preorder array and move its state to 2 (inorder) for this node. Push this updated state back onto the stack and push its left child as well.
            preorder.append(node.data)
            stack.append((node,2))
            if node.left:
                stack.append((node.left,1))
        elif state==2:                         #If the state is ‘2’ ie. inorder: store the node’s data is the inorder array and update its state to 3 (postorder) for this node. Push the updated state back onto the stack and push the right child onto the stack as well.
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
