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
def serialize(root):
    if root is None:
        return " "
    q=Queue()
    result=[]
    q.put(root)                 #put() is used with Python's Queue to add an element to the queue
    while not q.empty():
        current=q.get()
        if current is None:
            result.append("null")
            continue
        result.append(str(current.data))
        q.put(current.left)
        q.put(current.right)
    return ",".join(result)

def deserialize(result):
    if result==" ":
        return None
    values = result.split(",")
    q=Queue()
    root = node(int(values[0]))
    q.put(root)
    i = 1
    while not q.empty():
        current = q.get()
        # Left child
        if values[i] != "null":
            current.left = node(int(values[i]))
            q.put(current.left)
        i += 1
        # Right child
        if values[i] != "null":
            current.right = node(int(values[i]))
            q.put(current.right)
        i += 1
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
result=serialize(root)
same_root=deserialize(result)
print_tree(same_root)




    

