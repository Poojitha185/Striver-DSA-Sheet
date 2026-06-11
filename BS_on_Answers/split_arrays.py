def count_partitions(a, max_sum):
        partitions = 1  # at least one partition
        subarray_sum = 0  # current subarray sum

        for num in a:
            # Add to current subarray if it doesn't exceed max_sum
            if subarray_sum + num <= max_sum:
                subarray_sum += num
            else:
                # Start a new subarray
                partitions += 1
                subarray_sum = num
        return partitions
def largest_subarray_sum_minimized(a, k):
        low = max(a)  # minimum possible max sum
        high = sum(a)  # maximum possible max sum

        # Brute-force check
        for max_sum in range(low, high + 1):
            if count_partitions(a, max_sum) == k:
                return max_sum
        return low
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
k=int(input("enter the number of consecutive subarrays:"))
print("The largest sum among the subarrays:",largest_subarray_sum_minimized(arr, k))
