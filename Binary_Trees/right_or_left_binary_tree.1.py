#Time Complexity: O(N) In the worst case, we may visit every node in the binary tree exactly once. This happens when the tree is skewed (i.e., every node has only one child), effectively forming a linear structure. Hence, the time complexity becomes O(N), where N is the total number of nodes in the tree.
#Space Complexity: O(H),The space complexity depends on the height (H) of the binary tree due to the recursion stack in depth-first traversal (like preorder, inorder, postorder). In a balanced binary tree, the height is log₂N, leading to O(log N) space. However, in the worst case (a skewed tree), the height is N, resulting in O(N) space. So the space complexity is O(H), where H is the height of the tree.
#To get the left and right view of a Binary Tree, we perform a depth-first traversal of the Binary Tree while keeping track of the level of each node. For both the left and right view, we ensure that only the first node encountered at each level is added to the result vector.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def create_tree():
    data = int(input("Enter data (-1 for no node): "))
    if data == -1:
        return None
    root = Node(data)
    print("Enter left child of", data)
    root.left = create_tree()
    print("Enter right child of", data)
    root.right = create_tree()
    return root


#Here we use preorder traversal
#Check if the size of the result vector is equal to the current level. If true, it means that we have not yet encountered any node at this level in the result vector. Add the value of the current node to the result vector.
#Recursively call the function for the current node’s left child, then right child, with an increased level (level + 1).
#We call the left child first as we want to traverse the left-most nodes. If there is no left child, the recursion backtracks and explores the right child.

def leftDFS(node, level, res):
        # Base case
        if not node:
            return
        # If we are visiting the level for the first time
        if len(res) == level:
            res.append(node.val)
        # Recurse to left child
        leftDFS(node.left, level + 1, res)
        # Recurse to right child
        leftDFS(node.right, level + 1, res)

# Recursive function to get right view
# this is opposite to left view we first go to right child and then left child i.e reverse preorder traversal
def rightDFS(node, level, res):
        if not node:
            return
        if len(res) == level:
            res.append(node.val)
        # Recurse to right child
        rightDFS(node.right, level + 1, res)
        # Recurse to left child
        rightDFS(node.left, level + 1, res)

def leftView(root):
    res = []
    leftDFS(root, 0, res)
    return res

def rightView(root):
    res = []
    rightDFS(root, 0, res)
    return res

root = create_tree()
 # Get left and right view
left = leftView(root)
right = rightView(root)
print("Left View:", left)
print("Right View:", right)
