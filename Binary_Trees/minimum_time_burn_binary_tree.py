#Time Complexity: O(N), where N is the number of nodes in the binary tree. Every tree edge is added to the adjacency structure a constant number of times, and every node is processed at most once during BFS.
#Space Complexity: O(N). The adjacency list, burned set, and BFS queue can together store information for up to N nodes.

#Approach:
#A binary tree normally provides links only from a parent to its children. Burning, however, must be allowed to spread in both directions.
#Therefore, every parent-child connection is converted into an undirected edge. Once this conversion is performed, the tree behaves like an undirected graph in which the fire can move to every directly connected node.
#A BFS is then started from the target.
#A queue is used because nodes that burn at the same second must be processed together. The variable levelSize stores the number of nodes burning during the current second so that exactly one BFS level can be processed at a time.
#A set named burned is maintained to represent nodes that have already caught fire. It prevents the same node from being reached repeatedly through the bidirectional graph.
#A boolean variable spread is used to record whether at least one new node caught fire during the current BFS level. Time is increased only when spread becomes true, because a second should be counted only when the fire actually reaches another node.

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

#Build the Parent Map:
#Traverse the entire binary tree using either BFS or DFS and map each node to its parent node. This step effectively adds upward connectivity to the tree, allowing access to parent nodes during traversal.
#Create a parentMap where each key is a child node and its value is the corresponding parent node. This transforms the binary tree into an undirected structure where each node can move left, right, or up.
from queue import Queue
def parentnodes(root,parent_track):
    q=Queue()
    q.put(root)
    while not q.empty():
        cur=q.get()
        if cur.left:
            parent_track[cur.left]=cur
            q.put(cur.left)
        if cur.right:
            parent_track[cur.right]=cur
            q.put(cur.right)
    return parent_track
#finding the target node in the binary tree and using that node object we can perform BFS traversal from that node to find all nodes at distance K.
def find_target(root,target):
    if root is None:
        return None
    if root.data == target:
        return root
    left = find_target(root.left, target)
    if left:
        return left
    return find_target(root.right, target)

#Perform BFS from the Target Node:
#Begin a level-order (BFS) traversal from the target node to explore all nodes at increasing distances.
#Initialize a queue with the target node and a set to track visited nodes.
#For each node at the current BFS level:Visit the left child if it exists and hasn't been visited.Visit the right child if it exists and hasn't been visited.
def min_time_burn(root, target):
    parent_track={}
    parentnodes(root,parent_track)
    q=Queue()
    visited={}
    target_node = find_target(root, target)
    visited[target_node] = True
    q.put(target_node)
    time=0
    while not q.empty():
        f1=0
        j=q.qsize()
        for i in range(j):
            m=q.get()
            if m.left and m.left not in visited:
                f1=1
                q.put(m.left)
                visited[m.left] = True
            if m.right and m.right not in visited:
                f1=1
                q.put(m.right)
                visited[m.right] = True
            if m in parent_track and parent_track[m] not in visited:
                f1=1
                q.put(parent_track[m])
                visited[parent_track[m]] = True
        if f1:
            time+=1
    return time

root = create_tree()
target=int(input("enter the target node: "))
print("minimum time taken to burn entire binary tree:",min_time_burn(root,target))






