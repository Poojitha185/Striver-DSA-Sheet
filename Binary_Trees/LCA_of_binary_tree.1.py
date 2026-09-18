#LCA = the first/common meeting point when you travel UP from both nodes. And importantly, a node can be the LCA of itself and another node.
#Time Complexity: O(N), where N is the number of nodes in the binary tree. In the worst case, we may need to traverse all nodes to find the LCA.
#Space Complexity: O(H), where H is the height of the binary tree. This is due to the recursive stack space used during the traversal. In the worst case, for a skewed tree, H can be equal to N, but for a balanced tree, H will be log(N).class node:                   

#Start by checking if the current root node is null or matches one of the target nodes (x or y). If the root is null or matches either target node, return the root, as it could be the LCA or simply indicate the end of the search path.
#After completing the recursive searches, analyze the results of both subtree searches:  If both recursive calls return non-null values, it means one target node was found in each subtree. In this case, the current root node must be the LCA, as it is the common ancestor of both nodes.If only one of the subtree searches returns a non-null result, it implies both target nodes are located within the same subtree. Return the non-null result, which represents the LCA found in that subtree.

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

def dfs(root,p,q):
    if root is None or root.data==p or root.data==q:
        return root
    left=dfs(root.left,p,q)
    right=dfs(root.right,p,q)
    if left==None:
        return right
    elif right==None:
        return left
    else:
        return root
    
root=create_tree()

p=int(input("Enter the value of first node: "))
q=int(input("Enter the value of second node: "))

print("The LCA of the given nodes is:",dfs(root,p,q).data)