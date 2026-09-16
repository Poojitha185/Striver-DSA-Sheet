#LCA = the first/common meeting point when you travel UP from both nodes. And importantly, a node can be the LCA of itself and another node.
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
def dfs(root,p,q):
    if root is None or root.data==p or root.data==q:
        return root
    left=dfs(root.left,p,q)
    right=dfs(root.right,p,q)
    if left==None:
        return right
    elif right==None:
        return left
    else:
        return root
root=create_tree()
p=int(input("Enter the value of first node: "))
q=int(input("Enter the value of second node: "))
print("The LCA of the given nodes is:",dfs(root,p,q).data)