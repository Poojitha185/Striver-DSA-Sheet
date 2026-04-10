#TC:O(n logn),log n levels of splitting n work per level
#SC:O(N),Sorts in-place (modifies same array) But still uses extra memory internally. for Temporary arrays (for merging) and Storing runs (subarrays).
def sort_0_1_2(arr):
    arr.sort()
    return arr
arr=list(map(int,input("enter the array: ").split(',')))
print("The array after sorting the elements: ",sort_0_1_2(arr))