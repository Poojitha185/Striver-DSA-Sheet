#Time Complexity: O(N), we traverse the entire array once to find peak element.
#Space Complexity: O(1), constant additional space is used.
#A peak element is an element that is greater than or equal to its neighbors. To find a peak element in an array, we can iterate through the array and check if the current element is greater than or equal to its left and right neighbors. If it is, then we have found a peak element and we can return its index. If we reach the end of the array without finding a peak element, we can return -1.

def peak_element(arr,n):
    for i in range(n):
     left=(i==0)or(arr[i]>=arr[i-1])
     right=(i==n-1)or(arr[i]>=arr[i+1])
     if left and right:
        return i
    return -1
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The index of the peak element is:",peak_element(arr,n))