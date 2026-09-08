class node:                   #creates a blueprint/template for a tree node.
    def __init__(self,data):  #__init__ is a special Python method that runs automatically when you create an object.You could technically use another method, but then you'd have to call it yourself. __init__ is convenient because Python calls it automatically when the object is created.
        self.data=data        #self means the current Node object.
        self.left=None        #None simply means there is currently no child there.In Python, None is basically the equivalent of null in languages like C, C++, Java, and JavaScript.
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

from queue import Queue
def top_view(root):
    ans=[]
    dic={}
    q=Queue()
    q.put((root,0))              #put() is used with Python's Queue to add an element to the queue
    while not q.empty():
        front,line = q.get()
        if line not in dic:
            dic[line]=front.data
        if front.left:
            q.put((front.left,line-1))
        if front.right:
            q.put((front.right,line+1))
    for i in sorted(dic.keys()):
        ans.append(dic[i])
    return ans
# Create the tree
root = create_tree()
# Find traversals
print(top_view(root))