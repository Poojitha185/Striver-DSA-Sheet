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