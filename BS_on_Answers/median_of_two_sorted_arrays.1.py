# TC: O(log(min(m,n)))
# SC: O(1) because no extra data structure is used,
# Always perform binary search on the smaller array
# to achieve O(log(min(m,n))) complexity.
def median(arr1, arr2):
    m, n = len(arr1), len(arr2)

    # Always binary search on smaller array
    if m > n:
        return median(arr2, arr1)

    low = 0
    high = m

    while low <= high:
        cut1 = (low + high) // 2                              #cut1 = number of elements taken from arr1 into the left half.
        cut2 = (m + n + 1) // 2 - cut1                        #cut2 = remaining elements required from arr2 ,so that the left half contains exactly (m+n+1)//2 elements. 

        l1 = float('-inf') if cut1 == 0 else arr1[cut1 - 1]   #If cut1 is 0, it means we are not taking any elements from arr1 into the left half, so we assign l1 to negative infinity to ensure it does not affect the maximum calculation. Otherwise, l1 is the last element of the left half from arr1.
        l2 = float('-inf') if cut2 == 0 else arr2[cut2 - 1]   #If cut2 is 0, it means we are not taking any elements from arr2 into the left half, so we assign l2 to negative infinity to ensure it does not affect the maximum calculation. Otherwise, l2 is the last element of the left half from arr2.

        r1 = float('inf') if cut1 == m else arr1[cut1]
        r2 = float('inf') if cut2 == n else arr2[cut2]

        if l1 <= r2 and l2 <= r1:

            if (m + n) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2

            return max(l1, l2)

        elif l1 > r2:                     # If l1 > r2, we have taken too many elements from arr1, so move the cut to the left.
            high = cut1 - 1

        else:
            low = cut1 + 1
arr1=list(map(int,input("enter the first array: ").split(',')))
arr2=list(map(int,input("enter the first array: ").split(',')))
print("The median of 2 sorted arrays: ",median(arr1,arr2))