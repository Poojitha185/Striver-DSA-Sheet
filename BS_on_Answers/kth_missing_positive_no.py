def kth_missing_number(arr, k):
    for i in arr:
        if i <= k:
            k = k + 1
        else:
            break
    return k
arr = list(map(int, input("Enter the array: ").split(',')))
k = int(input("Enter the value of k: "))
print(kth_missing_number(arr, k))