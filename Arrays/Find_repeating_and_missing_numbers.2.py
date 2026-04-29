def repeating_and_missing_numbers(arr, n):
    sum_of_n = n * (n + 1) // 2
    sum_of_n_squared = n * (n + 1) * (2 * n + 1) // 6
    sum_of_n_array=0
    sum_of_n_squared_array=0
    for i in arr:
        sum_of_n_array+=i
        sum_of_n_squared_array+=i*i
    value1 = sum_of_n_array - sum_of_n
    value2 = sum_of_n_squared_array - sum_of_n_squared
    value2 = value2 // value1
    x=(value1 + value2) // 2
    y=x-value1
    return [int(x), int(y)]
arr = list(map(int, input("enter the array: ").split(',')))
n = len(arr)
print("The repeating and missing number in the array is:", repeating_and_missing_numbers(arr, n))
