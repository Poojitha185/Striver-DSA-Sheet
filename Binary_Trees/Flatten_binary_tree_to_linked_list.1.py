#Time Complexity: O(N), where N is the number of nodes in the binary tree. Every node is processed exactly once.
#Space Complexity: O(H), where H is the height of the binary tree, due to the recursion stack. This becomes O(N) for a skewed tree and O(log N) for a balanced tree.

#Approach:
# We need the nodes in preorder: Root -> Left -> Right.
# Use a stack to process nodes in preorder.
# Since stack follows LIFO, push the right child first and then the left child,
# so the left child comes out first.
# For every current node, make its right pointer point to the next node in preorder
# and set its left pointer to None.
# We are modifying the existing tree itself, so no new nodes are created.

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

def flatten_using_stack(root):
    if root is None:
        return
    stack=[]
    stack.append(root)
    while stack:
        cur=stack[-1]               #Getting top element from stack,stack is like python list to get top element we use stack[-1]
        stack.pop()
        if cur.right:
            stack.append(cur.right)
        if cur.left:                  # if use elif then if first condn executes it wont check elif so using if makes check all the condns
            stack.append(cur.left)
        if stack:
            cur.right=stack[-1]
        cur.left=None
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
new_root=flatten_using_stack(root)
print_tree(root)
