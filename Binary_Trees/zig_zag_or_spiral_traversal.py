#Time Complexity: O(N) where N is the number of nodes in the binary tree. Each node of the binary tree is enqueued and dequeued exactly once, hence all nodes need to be processed and visited. Processing each node takes constant time operations which contributes to the overall linear time complexity.
#Space Complexity: O(N) where N is the number of nodes in the binary tree. In the worst case, the queue has to hold all the nodes of the last level of the binary tree, the last level could at most hold N/2 nodes hence the space complexity of the queue is proportional to O(N). The resultant vector answer also stores the values of the nodes level by level and hence contains all the nodes of the tree contributing to O(N) space as well.

#Zigzag traversal is a modification of the traditional level order traversal in a binary tree. Level Order Traversal explores does at each level from left or right but zigzag traversal adds a twist by alternating the direction of exploration.
#At odd levels, we proceed from left to right but for even levels the order is reversed, from right to left. This is achieved by introducing a `leftToRight` flag which controls the order in which nodes are processed at each level.
#When `leftToRight` is true, nodes are inserted into the level vector from left to right and when its false, nodes are inserted right to left.

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