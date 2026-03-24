#Time Complexity:O(N2) for the worst and average cases and O(N) for the best case. Here, N = size of the array.bcz If no swaps happen → array is already sorted So we break early → Best Case = O(N)
#Space Complexity:O(1)
def bubble_sort(n,arr):
    for i in range(n-1,-1,-1):
        didswap=0
        for j in range(0,i):
            if arr[j]>arr[j+1]:
              arr[j],arr[j+1]=arr[j+1],arr[j]
              didswap=1
        if(didswap==0):
            break
    return arr
arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
print("Before using bubble sort the arary: ",arr)
print("After the bubble sort the array: ",bubble_sort(n,arr))