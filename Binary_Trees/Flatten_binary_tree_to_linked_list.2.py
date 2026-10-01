#Time Complexity: O(N), where N is the number of nodes in the binary tree. Although rightmost nodes of left subtrees are searched during rewiring, the traversal and pointer rearrangements together remain linear over the complete tree.
#Space Complexity: O(1), because the tree is modified in-place using only a constant number of pointers such as current and the rightmost-node pointer.

#The tree can also be flattened without storing nodes and without using recursion.
#A pointer named current is used to represent the node whose links are currently being rearranged. Whenever current has a left subtree, preorder traversal requires the entire left subtree to appear before the original right subtree: current → left subtree → right subtree Therefore, the left subtree must be moved to current.right.
#Before this can be done, the original right subtree must be preserved. A pointer can be moved to the rightmost node of the left subtree. This node is important because after the left subtree has been rewired into the right chain, it becomes the final node visited before preorder should continue into the original right subtree.
#The original right subtree is therefore attached to this rightmost node. The left subtree is then shifted to the right, and current.left is cleared.
#The process continues by moving current through the newly formed right pointers.

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