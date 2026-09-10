#Time Complexity: O(N) where N is the number of nodes in the binary tree. Each node of the binary tree is enqueued and dequeued exactly once, hence all nodes need to be processed and visited. Processing each node takes constant time operations which contributes to the overall linear time complexity.
#Space Complexity : O(N) where N is the number of nodes in the binary tree. In the worst case, the queue has to hold all the nodes of the last level of the binary tree, the last level could at most hold N/2 nodes hence the space complexity of the queue is proportional to O(N). The resultant vector answer also stores the values of the nodes level by level and hence contains all the nodes of the tree contributing to O(N) space as well.

#To get the left and right views of a binary tree, we use level order traversal (BFS). We queue nodes level by level. For each level, we record all node values in order. The left view is formed by picking the first node of each level, and the right view by picking the last node of each level.

from collections import deque

# Definition of tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:

    # Function to perform level order traversal
    def levelOrder(self, root):
        # Final 2D result list
        ans = []

        # Return empty if tree is empty
        if not root:
            return ans

        # Create queue for BFS
        q = deque()
        q.append(root)

        # Loop until queue is empty
        while q:
            # Get number of nodes at current level
            size = len(q)

            # List to hold current level values
            level = []

            # Process all nodes at this level
            for _ in range(size):
                # Pop node from queue
                node = q.popleft()

                # Store its value
                level.append(node.data)

                # Add left child if exists
                if node.left:
                    q.append(node.left)

                # Add right child if exists
                if node.right:
                    q.append(node.right)

            # Append this level to answer
            ans.append(level)

        return ans

    # Function to return left view
    def leftView(self, root):
        levels = self.levelOrder(root)
        return [level[0] for level in levels]

    # Function to return right view
    def rightView(self, root):
        levels = self.levelOrder(root)
        return [level[-1] for level in levels]

# Driver code
if __name__ == "__main__":
    # Build tree manually
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)

    # Create solution instance
    sol = Solution()

    # Get and print level order
    print("Level Order Traversal:")
    for level in sol.levelOrder(root):
        print(level)

    # Print left view
    print("Left View:", sol.leftView(root))

    # Print right view
    print("Right View:", sol.rightView(root))
