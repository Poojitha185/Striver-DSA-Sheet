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