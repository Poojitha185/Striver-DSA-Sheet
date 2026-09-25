#Time Complexity: O(N²) in the worst case. For each of the N nodes, its position may be searched linearly in the current inorder range. In a skewed tree, these searches can have sizes N, N-1, N-2, ..., resulting in quadratic time.
#Space Complexity: O(H), where H is the height of the constructed binary tree, due to the recursion stack. This becomes O(N) for a skewed tree and O(log N) for a balanced tree.

#Preorder traversal provides the most important information first: the root of the current subtree. Once that root is located in inorder, the inorder traversal divides the current subtree into: Left Subtree | Root | Right Subtree. This process can then be repeated recursively.
#A variable named preIndex is maintained to represent the index of the next unused element in preorder. Since preorder always visits the root before its children, preorder[preIndex] always gives the root of the subtree currently being constructed.
#Two variables, inStart and inEnd, represent the boundaries of the portion of the inorder array belonging to the current subtree. These boundaries prevent recursive calls from processing nodes that belong to some other subtree.
#For every newly selected root, its position is searched linearly between inStart and inEnd. This correctly divides the current subtree into its left and right portions.
#The repeated linear search makes this approach inefficient in the worst case.

class node:                   
    def __init__(self,data):  
        self.data=data        
        self.left=None        

def build_tree(inorder,preorder):
    pre_index = [0]
    return(build(preorder,inorder,0,len(inorder)-1,pre_index))

def build(preorder,inorder,in_start,in_end,pre_index):
        if in_start > in_end:
            return None
        root_value = preorder[pre_index[0]]
        pre_index[0] += 1
        root = node(root_value)
        root_index = in_start
        # The root position splits inorder
        # into left and right subtree ranges.
        while (root_index <= in_end and inorder[root_index] != root_value):    #linear search
            root_index += 1
        root.left = build( preorder,inorder,in_start,root_index - 1,pre_index)
        root.right = build(preorder,inorder,root_index + 1,in_end,pre_index)
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
preorder = list(map(int, input("Enter the preorder traversal of the binary tree: ").replace(",", " ").split()))
root = build_tree(inorder,preorder)
print_tree(root)

