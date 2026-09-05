#The diameter of a binary tree is the length of the longest path between any two nodes in the tree. It may or may not pass through the root.
#Time Complexity: O(N*N) where N is the number of nodes in the Binary Tree.
#Space Complexity : O(1) as no additional data structures or memory is allocated.
#To understand how wide a binary tree can be, imagine each point (node) in the tree as a possible turning point for the longest path. This turning point is where the path bends and includes the highest levels going left and right.
#At every turning point, the total width is found by adding how deep the left side goes and how deep the right side goes, plus one for the turning point itself. Total Width = 1 + Depth of Left Side + Depth of Right Side To find the widest path, we can go through the tree from top to bottom, checking each point as a turning point. At each one, we measure the left and right depth and calculate the width. The widest one we find during this process is the final answer.
#Keep a note of the largest width found so far. At every step, compare the current width with what we've stored, and always keep the bigger one.

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

def height(root):
    if root==None:
            return 0
    lt=height(root.left)
    rt=height(root.right)
    return 1+max(lt,rt)

def diameter(root):
    maxi=0
    if root==None:
          return 0
    lt=height(root.left)
    rt=height(root.right)
    maxi=max(maxi,lt+rt)
    lt=diameter(root.left)
    rt=diameter(root.right)
    return maxi

root=create_tree()
print("The diameter of binary tree: ",diameter(root))