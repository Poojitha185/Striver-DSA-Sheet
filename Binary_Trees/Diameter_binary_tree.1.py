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

diameter=0

def height(root,diameter):
    if root==None:
        return 0
    lt=height(root.left,diameter)
    rt=height(root.right,diameter)
    diameter[0]=max(diameter[0],lt+rt)
    return 1+max(lt,rt)
#List is used to share and update the same diameter value across recursive calls.# A normal integer would create a local copy, so changes would not be reflected outside. so diameter = [0]
def diameter_tree(root):
    diameter=[0]
    height(root,diameter)
    return diameter[0]

root=create_tree()
diameter=0
print("The diameter of binary tree: ",diameter_tree(root))
