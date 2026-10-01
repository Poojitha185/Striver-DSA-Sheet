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

def flatten(root): 
    cur=root 
    while(cur!=None):                    
        if cur.left!=None: 
            prev=cur.left 
            while(prev.right):  
                prev=prev.right                       
            prev.right=cur.right         #Last node of preoredr of left subtree is connected to root's first node of right subtree
            cur.right=cur.left 
            cur.left=None                      
        cur=cur.right 
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