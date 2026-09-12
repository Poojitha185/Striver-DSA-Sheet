#Time Complexity: O(N) In the worst case, we may visit every node in the binary tree exactly once. This happens when the tree is skewed (i.e., every node has only one child), effectively forming a linear structure. Hence, the time complexity becomes O(N), where N is the total number of nodes in the tree.

#Space Complexity: O(H),The space complexity depends on the height (H) of the binary tree due to the recursion stack in depth-first traversal (like preorder, inorder, postorder). In a balanced binary tree, the height is log₂N, leading to O(log N) space. However, in the worst case (a skewed tree), the height is N, resulting in O(N) space. So the space complexity is O(H), where H is the height of the tree.

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

    # Wrapper function for left view
def leftView(root):
    res = []
    leftDFS(root, 0, res)
    return res

    # Wrapper function for right view
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
