def first_occurrence(arr, n, target):
    low = 0
    high = n - 1
    first = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            first = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return first
def last_occurrence(arr, n, target):
    low = 0
    high = n - 1
    last = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            last = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return last
arr = list(map(int, input("Enter array: ").split(',')))
n = len(arr)
target = int(input("Enter target: "))
print([first_occurrence(arr,n,target),
       last_occurrence(arr,n,target)])