def insert(stack,temp):
    if not stack or stack[-1]<=temp:
        stack.append(temp)
        return
    val=stack.pop()
    insert(stack,temp)
    stack.append(val)
    
def sortstack(stack):
    if stack:
        temp=stack.pop()
        sortstack(stack)
        insert(stack,temp)
stack=list(map(int,input("enter the array: ").split(',')))
print("The sorted stack is:",end=" ")
sortstack(stack)
print(stack)
