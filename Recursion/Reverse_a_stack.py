#Time Complexity: O(n²), as each element is popped and inserted at the bottom (O(n) per element).

#Space Complexity: O(n), as only the recursion stack is used.
#Read the stack elements from the user.
#Pop the top element from the stack recursively until the stack becomes empty.
#While returning from recursion, insert each popped element at the bottom of the stack.
#Continue until all elements are inserted at the bottom in reverse order.


def insert_bottom(stack, temp):
    if not stack:
        stack.append(temp)
        return

    val = stack.pop()
    insert_bottom(stack, temp)
    stack.append(val)

def reverse(stack):
    if stack:
        temp=stack.pop()
        reverse(stack)
        insert_bottom(stack, temp)
stack=list(map(int,input("enter the array: ").split(',')))
print("The reversed stack is:",end=" ")
reverse(stack)
print(stack)