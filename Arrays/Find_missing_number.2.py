def missing_number(arr, n):
    total = n * (n + 1) // 2
    actual = sum(arr)
    return total - actual
arr = list(map(int, input("enter the first sorted arary: ").split(',')))
n = len(arr)
print("The missing number in the array is", missing_number(arr, n))