#The diameter of a binary tree is the length of the longest path between any two nodes in the tree. It may or may not pass through the root.
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

def height(root):
    if root==None:
            return 0
    lt=height(root.left)
    rt=height(root.right)
    return 1+max(lt,rt)

def diameter(root):
    maxi=0
    if root==None:
          return 0
    lt=height(root.left)
    rt=height(root.right)
    maxi=max(maxi,lt+rt)
    lt=diameter(root.left)
    rt=diameter(root.right)
    return maxi

root=create_tree()
print("The diameter of binary tree: ",diameter(root))