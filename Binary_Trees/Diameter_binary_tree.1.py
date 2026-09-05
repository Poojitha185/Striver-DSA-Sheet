#Time Complexity: O(N) where N is the number of nodes in the Binary Tree. This complexity arises from visiting each node exactly once during the postorder traversal.
#Space Complexity : O(H), where H is the height of the binary tree due to the recursion call stack (O(log N) for a balanced tree and O(N) for a skewed tree).
#The earlier method took extra time because it kept recalculating the depth of subtrees again and again. This repetition made the solution slower, especially for larger trees. To make it faster, we can work from the bottom of the tree upwards, calculating heights only once.
#Using a bottom-up approach called postorder traversal, we first finish work on the lower parts (left and right branches) before looking at the top (parent). This lets us measure the depth of each part and also check the diameter while going up the tree, all in one go.
#Start by keeping a place to store the largest diameter found. Make a function that, for each point, does the following: If the point doesn't exist, say the depth is zero. Otherwise, do the following:

#Measure how deep the left part goes, then do the same for the right part. Add the two depths and 1 (for the current point) to get the width at this point. Compare this width with the largest one we've seen so far and update it if it's bigger.


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

diameter=0

def height(root,diameter):
    if root==None:
        return 0
    lt=height(root.left,diameter)
    rt=height(root.right,diameter)
    diameter[0]=max(diameter[0],lt+rt)
    return 1+max(lt,rt)
#List is used to share and update the same diameter value across recursive calls.# A normal integer would create a local copy, so changes would not be reflected outside. so diameter = [0]
def diameter_tree(root):
    diameter=[0]
    height(root,diameter)
    return diameter[0]

root=create_tree()
diameter=0
print("The diameter of binary tree: ",diameter_tree(root))
