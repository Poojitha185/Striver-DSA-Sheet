def count_subarray_sum(arr,k,n):
    total=0
    for i in range(n):
        totalsum=0
        for j in range(i,n):
            totalsum +=arr[j]
            if totalsum==k:
                total+=1
    return total

arr=list(map(int,input("enter the array: ").split(',')))
k=int(input("enter the sum: "))
n=len(arr)
print("The count of subarrays with sum",k,"is: ",count_subarray_sum(arr,k,n))

            