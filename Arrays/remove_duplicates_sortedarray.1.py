#Time Complexity: O(N), We traverse the entire original array only once.
#Space Complexity: O(1), constant additional space is used to check unique elements.
#optimised solution using two pointers approach
def remove_duplicates(arr,n):
    i=0
    for j in range(1,n):
        if arr[i]!=arr[j]:
            arr[i+1]=arr[j]
            i=i+1
    return i+1
arr=arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
k=remove_duplicates(arr,n)
print("The number of unique elements are: ",k)
print("array after removing elements are:", arr[:k])