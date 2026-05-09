def first_last_occurrence(arr, n, target):
    first = -1
    last = -1
    for i in range(n):
        if arr[i] == target:
            if first == -1:
                first = i
            last = i
    return [first, last]
arr = list(map(int, input("Enter array: ").split(',')))
n = len(arr)
target = int(input("Enter target: "))
print(first_last_occurrence(arr, n, target))