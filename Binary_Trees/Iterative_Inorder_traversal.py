# Define the TreeNode structure
#Time Complexity: O(n), where n is the number of nodes in the binary tree. Each node is visited exactly once.

#Space Complexity: O(h), where h is the height of the binary tree. This is the space required for the stack to store the nodes during traversal.
class node:                   #creates a blueprint/template for a tree node.
    def __init__(self,data):  #__init__ is a special Python method that runs automatically when you create an object.You could technically use another method, but then you'd have to call it yourself. __init__ is convenient because Python calls it automatically when the object is created.
        self.data=data        #self means the current Node object.
        self.left=None        #None simply means there is currently no child there.In Python, None is basically the equivalent of null in languages like C, C++, Java, and JavaScript.
        self.right=None
        
class Solution:
    # Function to perform inorder traversal
    # of a binary tree iteratively
    def inorder(self, root):
        # Initialize a stack to track nodes
        st = []
        # Start from the root node
        node = root
        # Initialize a list to store
        # inorder traversal result
        inorder = []

        # Start an infinite
        # loop for traversal
        while True:
            # If the current node is not NULL
            if node is not None:
                # Push the current
                # node to the stack
                st.append(node)
                # Move to the left child
                # of the current node
                node = node.left
            else:
                # If the stack is empty,
                # break the loop
                if not st:
                    break
                # Retrieve a node from the stack
                node = st.pop()
                # Add the node's value to
                # the inorder traversal list
                inorder.append(node.data)
                # Move to the right child
                # of the current node
                node = node.right
        
        # Return the inorder
        # traversal result
        return inorder

# Creating a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Initializing the Solution class
sol = Solution()

# Getting the inorder traversal
result = sol.inorder(root)

# Displaying the inorder traversal result
print("Inorder Traversal:", result)
