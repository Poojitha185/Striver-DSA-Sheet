#Time Complexity: O(N) ,We visit each node exactly once when building the parent map using BFS ,O(N). We again visit each node at most once during the second BFS traversal from the target, O(N). Hence, the total time complexity is O(N), where N is the number of nodes in the binary tree.
#Space Complexity: O(N) , The parent map stores one entry per node,O(N). The queue and visited set used in BFS also take up to O(N) space in the worst case. Therefore, the total space complexity is O(N).

#In a binary tree, each node only has references to its children. To find all nodes at a specific distance K from a given target node, we must be able to move both downward (to children) and upward (to parent). Since the binary tree doesn’t store parent links, we simulate this by converting the tree into an undirected graph. This allows traversal in all directions: left, right, and parent. Once we treat the tree as a graph, we perform a standard Breadth-First Search (BFS) starting from the target node and collect all nodes that are exactly K steps away.

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
def find_target(root, target):
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
def print_nodes_distance_k(root, target, k,ans):
    parent_track={}
    parentnodes(root,parent_track)
    q=Queue()
    visited={}
    target_node = find_target(root, target)
    visited[target_node] = True
    q.put(target_node)
    cur_level=0 #distance
    while not q.empty():
        if cur_level==k:
            break
        cur_level+=1
        j=q.qsize()
        for i in range(j):
            m=q.get()
            if m.left and m.left not in visited:
                q.put(m.left)
                visited[m.left] = True
            if m.right and m.right not in visited:
                q.put(m.right)
                visited[m.right] = True
            if m in parent_track and parent_track[m] not in visited:
                q.put(parent_track[m])
                visited[parent_track[m]] = True
    while not q.empty():
            ans.append(q.get().data)
    return ans

root = create_tree()
target=int(input("enter the target node: "))
k=int(input("enter the distance value: "))
ans=[]
print_nodes_distance_k(root,target,k,ans)
print(ans)





