#Time Complexity:O(N^2),Selection sort runs in O(N²) time in the best, average, and worst cases due to its nested loop structure. It makes approximately N(N-1)/2 comparisons, regardless of the array's initial state. Even if no swaps are needed (best case), the number of comparisons remains the same./p>
#Space Complexity: O(1). No extra space used
def selection_sort(n,arr):
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
               min=j
        arr[min],arr[i]=arr[i],arr[min]
    return arr
arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
print("Before using selection sort the arary: ",arr)
print("After the selection sort the array: ",selection_sort(n,arr))