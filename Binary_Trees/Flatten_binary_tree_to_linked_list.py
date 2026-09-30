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

def reverse_preorder(root,prev):
    if root is None:
        return 
    reverse_preorder(root.right,prev)
    reverse_preorder(root.left,prev)
    root.right=prev[0]
    root.left=None
    prev[0]=root

def flatten(root):
    prev=[None]
    reverse_preorder(root,prev)
    return root

def print_tree(root):
    if root is None:
        print([])
        return
    queue = [root]
    result = []
    while queue:
        current = queue.pop(0)
        if current is None:
            result.append(None)
            continue
        result.append(current.data)
        queue.append(current.left)
        queue.append(current.right)
    while result[-1] is None:
        result.pop()
    print(result)
    
root=create_tree()
new_root=flatten(root)
print_tree(root)

