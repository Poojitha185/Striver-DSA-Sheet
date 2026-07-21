#Time Complexity: O(n2), where n is the number of elements in the stack.

#Space Complexity: O(n), due to the recursion stack.

#If the stack is empty, stop.Remove the top element of the stack.Sort the remaining stack recursively.
#Insert the removed element back into the stack while maintaining descending order. Use a helper function to place the element in its correct position.

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
