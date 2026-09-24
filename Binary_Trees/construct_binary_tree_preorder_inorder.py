#Time Complexity: O(N), where N is the number of nodes in the tree. The inorder index map is built once in O(N) time, and every node is created exactly once with O(1) average-time lookup of its inorder position.
#Space Complexity: O(N + H). The inorder index map stores N entries, while the recursion stack requires O(H) space. Since H ≤ N, the overall auxiliary space is O(N)

#The expensive operation in the brute-force approach is repeatedly searching for each root inside the inorder traversal.Because all values are distinct, every value has exactly one position in inorder. Therefore, a hash map can be created before reconstruction begins:node value → inorder indexThis allows each root position to be found in O(1) average time.
#The variable preIndex again represents the index of the next unused preorder value. Since preorder follows Root → Left → Right, the value at preorder[preIndex] is always the root of the current subtree.
#The variables inStart and inEnd represent the left and right boundaries of the inorder section belonging to that subtree. Once the current root's inorder index is obtained from the hash map, these boundaries can be divided directly into the ranges belonging to the left and right subtrees. Therefore: preorder determines which node becomes the root, inorder determines which nodes belong to its left and right subtrees.
#Each node is created exactly once, and repeated inorder scanning is eliminated.
class node:                   #creates a blueprint/template for a tree node.
    def __init__(self,data):  #__init__ is a special Python method that runs automatically when you create an object.You could technically use another method, but then you'd have to call it yourself. __init__ is convenient because Python calls it automatically when the object is created.
        self.data=data        #self means the current Node object.
        self.left=None        #None simply means there is currently no child there.In Python, None is basically the equivalent of null in languages like C, C++, Java, and JavaScript.
        self.right=None

def build_tree(inorder,preorder):
    pre_index = [0]
    inorder_ind={}
    for i in range(len(inorder)):
        inorder_ind[inorder[i]]=i
    return(build(preorder,0,len(inorder)-1,pre_index,inorder_ind))

def build(preorder,in_start,in_end,pre_index,inorder_ind):
        if in_start > in_end:
            return None
        root_value = preorder[pre_index[0]]
        pre_index[0] += 1
        root = node(root_value)
        # The stored inorder position divides. the current subtree into two ranges.
        root_index = inorder_ind[root_value]
        root.left = build( preorder,in_start,root_index - 1,pre_index,inorder_ind)
        root.right = build(preorder,root_index + 1,in_end,pre_index,inorder_ind)
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
inorder = list(map(int, input("Enter the inorder traversal of the binary tree: ").replace(",", " ").split()))
preorder = list(map(int, input("Enter the preorder traversal of the binary tree: ").replace(",", " ").split()))
root = build_tree(inorder,preorder)
print_tree(root)

