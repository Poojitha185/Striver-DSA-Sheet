#Time Complexity: O(N), every element of array is visited once.
#Space Complexity: O(1) , only constant variables are used.

def max_product_subarray(arr):
    curr_max = curr_min = ans = arr[0]

    for i in range(1, len(arr)):
        x = arr[i]

        if x < 0:
            curr_max, curr_min = curr_min, curr_max

        curr_max = max(x, curr_max * x)
        curr_min = min(x, curr_min * x)

        ans = max(ans, curr_max)

    return ans
arr = list(map(int, input("enter the array: ").split(',')))
print("The maximum product subarray is:", max_product_subarray(arr))