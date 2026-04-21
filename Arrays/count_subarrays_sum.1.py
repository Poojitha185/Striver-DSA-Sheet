#Time Complexity: O(n) We traverse the array once, where n is the size of the array. Each prefix sum operation and hashmap lookup is O(1) on average.

#Space Complexity: O(n) In the worst case, all prefix sums are distinct and stored in the hashmap, so space grows linearly with input size.

#using prefixsum stored in dictionary to count the number of subarrays with sum k approach
def count_subarrays_sum(arr,k,n):
    prefixsum_count={}
    count=0
    prefixsum=0
    prefixsum_count[0]=1
    for i in range(n):
        prefixsum+=arr[i]
        remove=prefixsum-k
        if remove in prefixsum_count:
            count+=prefixsum_count[remove]
        prefixsum_count[prefixsum]= prefixsum_count.get(prefixsum, 0) + 1
    return count
arr=list(map(int,input("enter the array: ").split(',')))
k=int(input("enter the sum: "))
n=len(arr)
print("The count of subarrays with sum",k,"is: ",count_subarrays_sum(arr,k,n))
            
