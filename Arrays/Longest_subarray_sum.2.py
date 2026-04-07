def longest_subarray_sum_k(arr, k):
    prefix_sum = 0
    max_len = 0
    seen = {}   # prefix_sum : index

    for i in range(len(arr)):
        prefix_sum += arr[i]

        # Case 1: from start
        if prefix_sum == k:
            max_len = i + 1
        # Case 2: check previous sum
        if (prefix_sum - k) in seen:
            length = i - seen[prefix_sum - k]
            max_len = max(max_len, length)
        # Store first occurrence
        if prefix_sum not in seen:
            seen[prefix_sum] = i

    return max_len
arr = list(map(int, input("enter the array: ").split(',')))
k = int(input("enter the sum(k) value: "))
print("The length of the longest subarray:", longest_subarray_sum_k(arr, k))