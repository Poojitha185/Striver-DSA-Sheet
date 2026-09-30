#Time Complexity: O(N), where N is the number of nodes in the binary tree. Every node is processed exactly once.
#Space Complexity: O(H), where H is the height of the binary tree, due to the recursion stack. This becomes O(N) for a skewed tree and O(log N) for a balanced tree.

#Storing the complete preorder traversal can be avoided by creating the required links while recursion returns.
#The desired flattened order is: Root → Left → Right
#If the tree is processed in the reverse order: Right → Left → Root
#a pointer named previous can be maintained. The name represents the node that should appear immediately after the current node in the final flattened preorder sequence.
#Once both subtrees have been processed, the current node can be connected directly to previous.

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

