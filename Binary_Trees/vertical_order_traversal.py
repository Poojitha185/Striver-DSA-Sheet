#Time Complexity: O(N * log²N * log²N * log²N), where N represents the number of nodes in the Binary Tree. Postorder traversal is performed using BFS with a time complexity of O(N), since each node is visited exactly once. Multiset operations for inserting overlapping nodes at specific vertical and horizontal levels take O(log²N) time. Map operations involve insertion and retrieval of nodes using vertical and level as keys. Since there are two nested maps, the total complexity becomes O(log²N * log²N).
#Space Complexity: O(N + N/2), where N represents the number of nodes in the Binary Tree. The map storing nodes based on vertical and level information occupies O(N) space, as it stores all N nodes of the tree. The queue for BFS traversal occupies space proportional to the maximum number of nodes at any level, which can be O(N/2) in the worst case for a balanced tree.
# This class defines a node in the binary tree
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
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
def findVertical(root):
        # Dictionary to store nodes by vertical and level
    nodes = {}
    q = Queue()
    q.put((root, 0, 0))
        # BFS loop
    while not q.empty():
            temp, x, y = q.get()
            # Insert into dictionary
            if x not in nodes:
                nodes[x] = {}                    #we need the second dictionary ,Because two nodes can have the same x but different y.
            if y not in nodes[x]:
                nodes[x][y] = []
            nodes[x][y].append(temp.data)
            if temp.left:
                q.put((temp.left, x - 1, y + 1))
            if temp.right:
                q.put((temp.right, x + 1, y + 1))

        # Prepare final result
    ans = []
    for x in sorted(nodes.keys()):
            col = []
            for y in sorted(nodes[x].keys()):
                col.extend(sorted(nodes[x][y]))    #using extend instead append(it adds list directly) bcz It takes the elements out of the list and adds them individually.bcz same level nodes store in the list and we need add them individually to column to add it in ans list as it contains vertical order traversal of each vertical line in listwise.
            ans.append(col)
    return ans

# Function to print result
def printResult(result):
    for level in result:
        print(" ".join(map(str, level)))    #Convert every item to a string → join them using spaces → print them. map(str, level) ,level contains integers join() needs strings. 
    print()

root=create_tree()
print("Vertical Traversal:")
printResult(findVertical(root))
