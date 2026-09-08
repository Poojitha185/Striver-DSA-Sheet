#Time Complexity: O(N) where N is the number of nodes in the Binary Tree. This complexity arises from visiting each node exactly once during the BFS traversal.
#Space Complexity: O(N/2 + N/2) where N represents the number of nodes in the Binary Tree. The main space consuming data structure is the queue used for BFS traversal. It acquires space proportional to the number of nodes in the level it is exploring hence in the worst case of a balanced binary tree, the queue will have at most N/2 nodes which is the maximum width.Additionally, the map is used to store the top view nodes based on their vertical positions hence its complexity will also be proportional to the greatest width level. In the worst case, it may have N/2 entries as well.

#To imagine the Binary Tree from above, we visualise vertical lines passing through the tree. Each vertical line represents a unique vertical position. Nodes to the right of the tree’s centre are assigned positive vertical indexes. As we move to the right, the vertical index increases. Nodes to the left of the tree’s centre are assigned negative vertical indexes. As we move to the left, the vertical index decreases.
#We use a map data structure to store the nodes corresponding to each vertical level 

class node:                   #creates a blueprint/template for a tree node.
    def __init__(self,data):  #__init__ is a special Python method that runs automatically when you create an object.You could technically use another method, but then you'd have to call it yourself. __init__ is convenient because Python calls it automatically when the object is created.
        self.data=data        #self means the current Node object.
        self.left=None        #None simply means there is currently no child there.In Python, None is basically the equivalent of null in languages like C, C++, Java, and JavaScript.
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
def top_view(root):
    ans=[]
    dic={}
    q=Queue()
    q.put((root,0))              #put() is used with Python's Queue to add an element to the queue
    while not q.empty():
        front,line = q.get()
        if line not in dic:
            dic[line]=front.data
        if front.left:
            q.put((front.left,line-1))     #ading tuple (front.left, line-1) to the queue. The left child is associated with a vertical index decremented by 1.
        if front.right:
            q.put((front.right,line+1))
    for i in sorted(dic.keys()):
        ans.append(dic[i])
    return ans

# Create the tree
root = create_tree()
# Find traversals
print(top_view(root))