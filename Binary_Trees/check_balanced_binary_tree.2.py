#Time Complexity: O(N), where N is the number of nodes in the Binary Tree. Each node is visited exactly once during the postorder traversal.

#Space Complexity: O(1), since no extra data structures are used that grow with input size. However, O(H) auxiliary space is used by the recursion stack, where H is the height of the tree. In the best case (balanced tree), H = log₂N; in the worst case (skewed tree), H = N.

#The O(N²) time complexity of the previous approach can be optimized by checking the balance condition while traversing the tree in a bottom-up manner. Instead of repeatedly calculating the height at each node, we compute subtree heights during postorder traversal and evaluate the balance condition at the same time.
#This avoids redundant height calculations and allows early detection of unbalanced nodes, thereby preventing unnecessary recursive calls. Postorder traversal helps ensure that we already have the height information of both subtrees when we assess the balance condition at any node.
#Traverse the Binary Tree in post-order using recursion: visit the left subtree, then the right subtree, and finally the current node.
#Check the absolute difference between the heights of the left and right subtrees. If the difference is greater than 1, or if either subtree is already unbalanced (returns -1), return -1 to indicate an unbalanced state.
#Continue the traversal until all nodes are visited. If no -1 is returned, the tree is balanced.

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

def maximum_depth(root):
    if root==None:
        return 0
    lt=maximum_depth(root.left)
    if lt==-1:
        return -1
    rt=maximum_depth(root.right)
    if rt==-1:
        return -1
    if abs(lt-rt)>1:
        return -1
    return 1+max(lt,rt)

root=create_tree()

def is_balanced(root):
  if(maximum_depth(root)==-1):
    return False
  return True

print(is_balanced(root))