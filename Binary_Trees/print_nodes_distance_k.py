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
def find_target(root, target):
    if root is None:
        return None
    if root.data == target:
        return root
    left = find_target(root.left, target)
    if left:
        return left
    return find_target(root.right, target)

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





