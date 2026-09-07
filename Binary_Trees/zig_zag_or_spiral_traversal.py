
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

from queue import Queue
def zig_zag_traversal(root):
    if root is None:
        return []
    q = Queue()
    flag = 0
    ans = []
    q.put(root)
    while not q.empty():
        size = q.qsize()
        row = []
        for i in range(size):
            front = q.get()

            row.append(front.data)

            if front.left is not None:
                q.put(front.left)

            if front.right is not None:
                q.put(front.right)
        if flag == 1:
            row.reverse()
        ans.append(row)
        flag = 1-flag
    return ans
root=create_tree()
print("Zig-Zag traversal of the binary tree is:", zig_zag_traversal(root))