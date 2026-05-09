#TC: O(N), where N is the size of the array. This is because we are iterating through the array once to find the target element.
#SC: O(1), as we are using a constant amount of space for variables, regardless of the input size.

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