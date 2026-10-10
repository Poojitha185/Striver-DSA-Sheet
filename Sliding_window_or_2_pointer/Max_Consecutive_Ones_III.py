#Time Complexity: O(N²), where N represents the array size. Expansion from every starting index may traverse most of the remaining array.
#Space Complexity: O(1), because only index variables, zeroCount, and maxLength require auxiliary storage.

#Every contiguous subarray represents a possible group of consecutive 1s after flipping the zeroes present inside the range. A subarray remains valid as long as the zero count does not exceed k.
#Starting from every index and expanding toward the right examines every possible candidate. Expansion from one start can stop immediately after the zero count exceeds k because adding more elements cannot reduce the number of zeroes already present.

def max_consecutive_ones(nums,n,k):    #or longest_subarray_with_atmost_kzeros
    maxlen=0
    for i in range(n): 
        zeroslen=0
        for j in range(i,n):
            if nums[j]==0:
                zeroslen+=1
            if zeroslen<=k:
                length=j-i+1
                maxlen=max(maxlen,length)
            else:
                break
    return maxlen

nums = list(map(int, input("Enter the array of 0s and 1s: ").split(",")))
n=len(nums)
k=int(input("enter the value of k(no of zeros allowed):"))
print("The length of the longest subarray with at most k zeros: ",max_consecutive_ones(nums,n,k))