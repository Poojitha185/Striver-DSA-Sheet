#Time Complexity: O(N2), where N is the number of nodes in the binary tree. For each node, we calculate the height of its left and right subtrees, and height calculation takes O(N) in the worst case, leading to an overall O(N × N) = O(N²).
#Space Complexity: O(H), where H is the height of the tree. This space is used by the recursive call stack of the getHeight function. In the worst case (skewed tree), H = N, and in the best case (balanced tree), H = log N. No additional data structures are used, so auxiliary space remains constant.

#Base Case: If the root is null, it indicates an empty tree, which is considered balanced. So, return true.
#Use a helper function like getHeight to recursively calculate the height of the left and right subtrees.
#Store the height of the left subtree in a variable and the right subtree in another variable.
#Check if the absolute difference between the two heights is less than or equal to 1.
#If this condition holds, recursively call the isBalanced function on the left and right child nodes. If both subtrees are balanced and the current node also satisfies the height condition, return true. If the height difference is more than 1 or any subtree is unbalanced, return false.

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

def isBalanced( root):
        # If the tree is empty, it's balanced
        if root is None:
            return True
        # Calculate the height of left and right subtrees
        leftHeight = getHeight(root.left)
        rightHeight = getHeight(root.right)
        # Check if the absolute difference in heights of left and right subtrees is <= 1
        if abs(leftHeight - rightHeight) <= 1 and isBalanced(root.left) and isBalanced(root.right):         #abs() is a built-in Python function that returns the absolute value of a number. In simple words: it removes the negative sign.
            return True
        # If any condition fails, the tree is unbalanced
        return False
    # Function to calculate the height of a subtree
def getHeight(root):
        # Base case: if the current node is NULL, return 0 (height of an empty tree)
        if root is None:
            return 0
        # Recursively calculate the height of left and right subtrees
        leftHeight = getHeight(root.left)
        rightHeight = getHeight(root.right)
        # Return the maximum height of left and right subtrees plus 1 (for the current node)
        return max(leftHeight, rightHeight) + 1

root=create_tree()
print("is the binary tree balanced?",isBalanced(root) )