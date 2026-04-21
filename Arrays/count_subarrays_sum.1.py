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
            
