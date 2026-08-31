#Time Complexity: O(N), each node is processed once in Level Order Traversal.
#Space Complexity: O(N), in worst case, a maximum of N/2 nodes can be present in queue.
#To find the depth (or height) of a binary tree using BFS, we can take advantage of level-order traversal. Since each level of the tree corresponds to one unit of depth, we can traverse the tree level by level, and the number of levels we visit gives us the depth.
#Begin a loop that continues until the queue becomes empty where at each level:
#Increment `level` by 1, indicating we are moving to the next level.
#Determine the number of nodes at the current level by storing the size of the queue.
#Iterate over the number of nodes equal to the size of the queue and at each node, Pop it from front of the queue and push its left and right children (if they exist).

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
def max_depth(root):
    if root is None:
        return 0
    q=Queue()
    level=0
    q.put(root)                 #put() is used with Python's Queue to add an element to the queue
    while not q.empty():
        size=q.qsize()          #qsize() simply means “queue size”. It tells you how many elements are currently inside the queue.
        for i in range(size):
            front = q.get()      # Get the front node in the queue
            if front.left is not None: 
                q.put(front.left) # Enqueue left child if exists
            if front.right is not None: 
                q.put(front.right) # Enqueue right child if exists
        level += 1
    return level

root=create_tree()
print("Maximum depth of the binary tree is:", max_depth(root))