#Time Complexity: O(N), where N is the number of nodes in the tree. The inorder index map is built once in O(N) time, and every node is created exactly once with O(1) average-time lookup of its inorder position.
#Space Complexity: O(N + H). The inorder index map stores N entries, while the recursion stack requires O(H) space. Since H ≤ N, the overall auxiliary space is O(N)

class node:                   
    def __init__(self,data):  
        self.data=data        
        self.left=None        

def build_tree(inorder,postorder):
    k=len(postorder)-1
    post_index = [k]
    inorder_ind={}
    for i in range(len(inorder)):
        inorder_ind[inorder[i]]=i
    return(build(postorder,0,len(inorder)-1,post_index,inorder_ind))

def build(postorder,in_start,in_end,post_index,inorder_ind):
        if in_start > in_end:
            return None
        root_value = postorder[post_index[0]]
        post_index[0] -= 1
        root = node(root_value)
    # Postorder traversal is: LEFT -> RIGHT -> ROOT.
    # Since we start reading postorder from the END,
    # the order becomes: ROOT -> RIGHT -> LEFT.
    # Therefore, after creating the root, we must build
    # the RIGHT subtree first and then the LEFT subtree.
        root_index = inorder_ind[root_value]
        root.right = build(postorder,root_index + 1,in_end,post_index,inorder_ind)
        root.left = build( postorder,in_start,root_index - 1,post_index,inorder_ind)
        
        return root
#printing the binary tree
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
    
inorder = list(map(int, input("Enter the inorder traversal of the binary tree: ").replace(",", " ").split()))
postorder = list(map(int, input("Enter the postorder traversal of the binary tree: ").replace(",", " ").split()))
root = build_tree(inorder,postorder)
print_tree(root)

