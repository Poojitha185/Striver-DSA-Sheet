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

def find_path(root, target, path):
    if root is None:
        return False
    path.append(root.data)
    if root.data == target:
        return True
    if find_path(root.left, target, path) or find_path(root.right, target, path):
        return True
    path.pop()
    return False

def lca(root, p, q):
    path1 = []
    path2 = []
    find_path(root, p, path1)
    find_path(root, q, path2)
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]

root=create_tree()
p=int(input("Enter the value of first node: "))
q=int(input("Enter the value of second node: "))
print("The LCA of the given nodes is:",lca(root, p, q))