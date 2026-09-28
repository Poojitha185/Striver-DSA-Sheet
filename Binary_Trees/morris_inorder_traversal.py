# TC: O(N) ,Each node is processed a constant number of times.
# SC: O(1),Morris traversal does not use recursion or a stack.
# Note: inorder_list itself takes O(N) space for storing the output.
#Inorder traversal visits the nodes of a binary tree in the following order: Left Subtree → Root → Right Subtree
#The usual recursive method uses the call stack to remember how to return to a node after processing its left subtree. An iterative method replaces the recursion stack with an explicit stack. Both methods require additional space proportional to the height of the tree ,O(H)
#Morris Inorder Traversal performs the same traversal without recursion and without an explicit stack. It temporarily creates links inside the tree so that traversal can return from a node’s left subtree to the node itself.
# #After using a temporary link, Morris traversal removes it. Therefore, the original tree structure is restored before the traversal finishes.
#The major advantage is: Auxiliary Space Complexity: O(1)

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

def inorder(root):
    cur=root
    inorder_list=[]
    while(cur!=None):                    #tc:o(n)
        if cur.left==None:
            inorder_list.append(cur.data)
            cur=cur.right
        else:
            prev=cur.left
            while(prev.right and prev.right!=cur): 
                prev=prev.right
            if prev.right==None:
                prev.right=cur                        # creating temporary link to get back to root
                cur=cur.left
            else:
                prev.right=None                       # removing temporary link after getting back to root
                inorder_list.append(cur.data)
                cur=cur.right
    return inorder_list
root=create_tree()
print("The inorder traversal of binary tree: ",inorder(root))

