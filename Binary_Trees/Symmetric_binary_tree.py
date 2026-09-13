class Node:
    def __init__(self, val):
        self.data = val
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

def symmetric(left,right):
    if left is None or right is None:
        return left==right
    if(left.data!=right.data):
        return False
    return symmetric(left.left,right.right) and symmetric(left.right,right.left)
def issymmetric(root):
    if root is None:
        return True
    else:
        return symmetric(root.left,root.right)
root = create_tree()
print(issymmetric(root))