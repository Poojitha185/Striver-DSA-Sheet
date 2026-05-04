# This function returns the maximum product subarray
# using prefix and suffix traversal

#Time Complexity: O(N), every element of array is visited once.
#Space Complexity: O(1), constant number of variables are used.

def max_product_subarray(arr):
    prefix = 1
    suffix = 1
    maxi = float('-inf')
    n = len(arr)

    for i in range(n):
        prefix *= arr[i]
        suffix *= arr[n - 1 - i]

        maxi = max(maxi, prefix, suffix)

        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1

    return maxi
arr = list(map(int, input("enter the array: ").split(',')))
print("The maximum product subarray is:", max_product_subarray(arr))