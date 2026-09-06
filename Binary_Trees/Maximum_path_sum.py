#Time Complexity: O(N), each node is processed once in DFS Traversal.
#Space Complexity: O(H), auxiliary stack space, where H is height of Binary Tree.

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


def height(root,maximum_path):
    if root==None:
        return 0
    lt=height(root.left,maximum_path)
    rt=height(root.right,maximum_path)
    current_path=root.data+lt+rt                 #current_path is just a temporary variable, so you don't need to initialise it outside the function.
    maximum_path[0]=max(maximum_path[0],current_path)
    return root.data+max(lt,rt)                  #Return one-sided path

def maximum_sum(root):
    maximum_path=[float('-inf')]
    height(root,maximum_path)
    return maximum_path[0]
root=create_tree()
print("The maximum path sum is: ",maximum_sum(root))