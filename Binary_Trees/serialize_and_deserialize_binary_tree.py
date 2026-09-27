#Time Complexity: O(N) for both serialization and deserialization because the sequence contains only O(N) node values and null markers.
#Space complexity: O(N) because the complete serialized representation is stored as a string. Auxiliary Queue Space: O(W) because the queue may simultaneously store nodes from the widest part of the tree. Since W ≤ N, the queue requires O(N) auxiliary space in the worst case. The reconstructed tree itself requires O(N) space, but it is the required output of deserialization and is not counted as auxiliary space.

#The tree can also be serialized level by level using BFS.
#A queue is used to process nodes from top to bottom. For every non-null node, its value is recorded and its two child positions are added to the queue. When a child is missing, null is recorded. These null markers preserve the exact left and right positions of every child.
#During deserialization, the first token is used to create the root. The remaining tokens are consumed in pairs for every parent removed from the queue: The first token represents its left child. The second token represents its right child.
#The tree is therefore reconstructed level by level.

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




    

