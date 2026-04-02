#TC:O(N),at worst case and average case if element is not there or at last index andO(1) at best case if element is at first index
#SC:O(1)
def linear_search(arr,n,target):
    for i in range(n):
        if arr[i]==target:
            return i
    return -1
arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
target=int(input("enter the element to be search: "))
val=linear_search(arr,n,target)
if val!=-1:
 print("The element", target, "found at", val, "th index")
else:
   print("The element", target, "not found in the array")