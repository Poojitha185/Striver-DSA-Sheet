#Time Complexity: O(N log N), where N is the size of the array, due to the sorting step.
#Space Complexity: O(1), as we are using a constant amount of extra space.
def second_largest(arr,n):
    arr.sort()
    large=arr[-1]
    for i in range(n-2, -1, -1):
        if arr[i] != large:
            return arr[i]
    return -1  
arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
print("the second largest element of an array: ",second_largest(arr,n))