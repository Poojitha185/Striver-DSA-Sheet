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