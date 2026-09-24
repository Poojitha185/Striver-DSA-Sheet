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

