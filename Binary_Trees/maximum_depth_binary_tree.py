
class node:                   
    def __init__(self,data):    
        self.data=data        
        self.left=None         
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

def maximum_depth(root):
    if root==None:
        return 0
    lt=maximum_depth(root.left)
    rt=maximum_depth(root.right)
    return 1+max(lt,rt)
root=create_tree()
print("Maximum depth of the binary tree is:", maximum_depth(root))