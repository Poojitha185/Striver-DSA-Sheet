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
    #If at least one node is empty, check whether BOTH are empty.
    if left is None or right is None:         
        return left==right                          #left == right → compares whether they are the same node/address(comparing objects not data of them)  
    #if both are not none then will compare their data 
    if(left.data!=right.data):
        return False
    return symmetric(left.left,right.right) and symmetric(left.right,right.left)  #simultaneously traversing left and right subtree of root ,traversing left subtree in inorder fashion whereas right subtree in reverse inorder fashion
def issymmetric(root):
    if root is None:
        return True
    else:
        return symmetric(root.left,root.right)
root = create_tree()
print(issymmetric(root))