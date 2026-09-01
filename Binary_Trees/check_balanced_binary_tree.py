
class node:                   
    def __init__(self,data):    
        self.data=data        
        self.left=None         
        self.right=None
tree_data=[]                 #it contains node objects but not the values of the nodes. and objects also iterable in list. So, we can iterate over the list of node objects and access their left and right children to check if the tree is balanced or not.
def create_tree():
    data = int(input("Enter data (-1 for no node): "))
    if data == -1:
        return None
    root = node(data)
    tree_data.append(root)  
    print("Enter left child of", data)
    root.left = create_tree()
    print("Enter right child of", data)
    root.right = create_tree()
    return root

def maximum_depth(root):
    if root==None:
        return 0
    lt=maximum_depth(root.left)
    rt=maximum_depth(root.right)
    return 1 + max(lt, rt)


# Checks every node
def is_balanced(tree_data):
    for i in tree_data:
        # Find left and right subtree heights
        lt = maximum_depth(i.left)
        rt = maximum_depth(i.right)
        # Calculate balance factor
        balance = lt - rt
        if balance > 1 or balance < -1:
            return False
    return True


root=create_tree()
print("is the binary tree balanced?",is_balanced(tree_data) )