#Time Complexity: O(N * log²N * log²N * log²N), where N represents the number of nodes in the Binary Tree. Postorder traversal is performed using BFS with a time complexity of O(N), since each node is visited exactly once. Multiset operations for inserting overlapping nodes at specific vertical and horizontal levels take O(log²N) time. Map operations involve insertion and retrieval of nodes using vertical and level as keys. Since there are two nested maps, the total complexity becomes O(log²N * log²N).
#Space Complexity: O(N + N/2), where N represents the number of nodes in the Binary Tree. The map storing nodes based on vertical and level information occupies O(N) space, as it stores all N nodes of the tree. The queue for BFS traversal occupies space proportional to the maximum number of nodes at any level, which can be O(N/2) in the worst case for a balanced tree.
# This class defines a node in the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
# This class contains the solution logic
class Solution:
    # Function to perform vertical order traversal
    def findVertical(self, root):
        # Dictionary to store nodes by vertical and level
        nodes = {}
        # Queue for BFS traversal
        from collections import deque, defaultdict
        todo = deque()
        todo.append((root, 0, 0))

        # BFS loop
        while todo:
            temp, x, y = todo.popleft()

            # Insert into dictionary
            if x not in nodes:
                nodes[x] = {}
            if y not in nodes[x]:
                nodes[x][y] = []
            nodes[x][y].append(temp.data)

            # Left child
            if temp.left:
                todo.append((temp.left, x - 1, y + 1))
            # Right child
            if temp.right:
                todo.append((temp.right, x + 1, y + 1))

        # Prepare final result
        ans = []
        for x in sorted(nodes.keys()):
            col = []
            for y in sorted(nodes[x].keys()):
                col.extend(sorted(nodes[x][y]))
            ans.append(col)

        return ans

# Function to print result
def printResult(result):
    for level in result:
        print(" ".join(map(str, level)))
    print()

# Driver code
if __name__ == "__main__":
    # Create sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(10)
    root.left.left.right = Node(5)
    root.left.left.right.right = Node(6)
    root.right = Node(3)
    root.right.right = Node(10)
    root.right.left = Node(9)

    # Create solution object
    solution = Solution()

    # Call function
    verticalTraversal = solution.findVertical(root)

    # Print result
    print("Vertical Traversal:")
    printResult(verticalTraversal)
