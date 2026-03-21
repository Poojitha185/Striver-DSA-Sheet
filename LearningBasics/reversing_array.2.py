#using builtin function approach 
# TC:O(N) , because each element is visited once and possibly swapped once with its mirror index.
# SC: O(1) for C++, Java, and JavaScript (in-place), but O(n) for Python slicing since it creates a new list and then assigns back (unless using two pointers).
def reverse(arr):
    arr[:]=arr[::-1]
    return arr
n=int(input("enter the number of elements: "))
print("enter array elements: ")
m=[]
for i in range(n):
      m.append(int(input()))
print(reverse(m))