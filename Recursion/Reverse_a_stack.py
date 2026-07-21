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