#Time Complexity: O(N), where N represents the array size. Pointer right processes every element once, while pointer left only moves forward across the array.
#Space Complexity: O(1), because only two pointers, zeroCount, and maxLength require auxiliary storage.

#optimal approach 2 without using while loop inside. moving left pointer and it doesn't allow maxlength to change until it  came across the zeros, reducing zero count <= k

#A sliding window can represent the current subarray capable of becoming all 1s. The window remains valid while the number of zeroes stays at most k.
#Pointer right expands the window and explores longer candidates. After the zero count exceeds k, pointer left removes elements until the window becomes valid again. Every pointer moves only forward, eliminating repeated examination of the same subarrays.

def max_consecutive_ones(nums,n,k):    #or longest_subarray_with_atmost_kzeros
    maxlen=0
    zeros=0
    left,right=0,0
    while(right<n):                     #tc:O(n)
            if nums[right]==0:
                zeros+=1
                if zeros>k:
                    if nums[left]==0:
                        zeros-=1
                    left+=1      
            if zeros<=k:
                length=right-left+1
                maxlen=max(maxlen,length)
            right+=1
    return maxlen

nums = list(map(int, input("Enter the array of 0s and 1s: ").split(",")))
n=len(nums)
k=int(input("enter the value of k(no of zeros allowed): "))
print("The length of the longest subarray with at most k zeros: ",max_consecutive_ones(nums,n,k))