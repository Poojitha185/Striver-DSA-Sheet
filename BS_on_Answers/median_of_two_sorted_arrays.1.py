def median(arr1, arr2):
    m, n = len(arr1), len(arr2)

    # Always binary search on smaller array
    if m > n:
        return median(arr2, arr1)

    low = 0
    high = m

    while low <= high:
        cut1 = (low + high) // 2
        cut2 = (m + n + 1) // 2 - cut1

        l1 = float('-inf') if cut1 == 0 else arr1[cut1 - 1]
        l2 = float('-inf') if cut2 == 0 else arr2[cut2 - 1]

        r1 = float('inf') if cut1 == m else arr1[cut1]
        r2 = float('inf') if cut2 == n else arr2[cut2]

        if l1 <= r2 and l2 <= r1:

            if (m + n) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2

            return max(l1, l2)

        elif l1 > r2:
            high = cut1 - 1

        else:
            low = cut1 + 1
arr1=list(map(int,input("enter the first array: ").split(',')))
arr2=list(map(int,input("enter the first array: ").split(',')))
print("The median of 2 sorted arrays: ",median(arr1,arr2))