#Time Complexity: O(N²), because maximum depth is calculated separately for every node, causing repeated traversal.
#Space Complexity: O(N), because all nodes are stored in tree_data and recursion can take O(N) stack space in the worst case.
#using recursion and data structure to iterate over the nodes of the tree to check if it is balanced or not. A binary tree is considered balanced if for every node, the height difference between its left and right subtrees is at most 1. 
#The algorithm first constructs the binary tree and stores all its nodes in a list called tree_data. Then, for each node in tree_data, it calculates the maximum depth of its left and right subtrees using a recursive function maximum_depth. It computes the balance factor by subtracting the right subtree height from the left subtree height. If the balance factor exceeds 1 or is less than -1 for any node, the function returns False, indicating that the tree is not balanced. If all nodes satisfy the balance condition, it returns True, confirming that the tree is balanced.

class node:                   
    def __init__(self,data):    
        self.data=data        
        self.left=None         
        self.right=None
        
tree_data=[]                 #it contains node objects but not the values of the nodes. and objects also iterable in list. So, we can iterate over the list of node objects and access their left and right children to check if the tree is balanced or not.
def create_tree():
    data = int(input("Enter data (-1 for no node): "))
    if data == -1:
        return None
    root = node(data)
    tree_data.append(root)  
    print("Enter left child of", data)
    root.left = create_tree()
    print("Enter right child of", data)
    root.right = create_tree()
    return root

def maximum_depth(root):
    if root==None:
        return 0
    lt=maximum_depth(root.left)
    rt=maximum_depth(root.right)
    return 1 + max(lt, rt)


# Checks every node
def is_balanced(tree_data):
    for i in tree_data:
        # Find left and right subtree heights
        lt = maximum_depth(i.left)
        rt = maximum_depth(i.right)
        # Calculate balance factor
        balance = lt - rt
        if balance > 1 or balance < -1:
            return False
    return True


root=create_tree()
print("is the binary tree balanced?",is_balanced(tree_data) )