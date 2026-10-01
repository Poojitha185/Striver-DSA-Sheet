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
