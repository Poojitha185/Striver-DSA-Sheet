def repeating_and_missing_numbers(arr, n):
    k = {}
    repeating = 0
    missing = 0
    for i in arr:
        k[i] = k.get(i, 0) + 1
    for i in range(1, n+1):
        if k.get(i, 0) == 2:
            repeating = i
        elif k.get(i, 0) == 0:
            missing = i

    return [repeating, missing]


arr = list(map(int, input("enter the array: ").split(',')))
n = len(arr)
print("The repeating and missing number in the array is:", repeating_and_missing_numbers(arr, n))