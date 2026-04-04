#TC:O(N), O(N)  (set creation)+ O(N × 1) (loop + constant check)= O(N)
#SC:O(N), as we are using a set to store the elements of the array, which can take up to O(N) space in the worst case when all elements are distinct.
def missing_number(arr, n):
    s=set(arr)                 #To make searching fast (O(1)) Instead of checking in list (O(N))
    for i in range(1,n+1):
        if i not in s:
            return i
arr=list(map(int,input("enter the first sorted arary: ").split(',')))
n=len(arr)
print("The missing number in the array is",missing_number(arr,n+1))