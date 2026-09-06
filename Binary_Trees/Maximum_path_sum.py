#Time Complexity: O(N), each node is processed once in DFS Traversal.
#Space Complexity: O(H), auxiliary stack space, where H is height of Binary Tree.
#To find the maximum sum path in a binary tree, we treat every node as a possible turning point. At each node, we calculate the maximum path sum by adding the node’s value to the maximum path sums from its left and right subtrees.
#Use a recursive function that explores each node in the tree, calculating the best path sum from its left and right branches. If a node is null, treat its path sum as zero.
#For each node, calculate the total path sum by adding the current node's value and the sums from both its left and right branches.
#Update the tracked maximum path sum if this total is larger than what we had before.

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

#We can solve the maximum path sum problem using recursively traversing the tree and treating each node as a possible turning point. At every node, we calculate two things:
#The maximum path sum that passes through the current node (left + right + node value). This is used to update our global maximum.
#The maximum path sum from the current node down one side (either left or right), which we return to the parent call.
#If a node is null, we return 0 since it doesn’t contribute to the path. This way, we explore all possible paths and keep track of the highest one found.
def height(root,maximum_path):
    if root==None:
        return 0
    lt=height(root.left,maximum_path)
    rt=height(root.right,maximum_path)
    current_path=root.data+lt+rt                 #current_path is just a temporary variable, so you don't need to initialise it outside the function.
    maximum_path[0]=max(maximum_path[0],current_path)
    return root.data+max(lt,rt)                  #Return one-sided path. Return the best one-sided path (either left or right plus the current node) to be used in calculations above in the recursion.

def maximum_sum(root):
    maximum_path=[float('-inf')]
    height(root,maximum_path)
    return maximum_path[0]

root=create_tree()
print("The maximum path sum is: ",maximum_sum(root))