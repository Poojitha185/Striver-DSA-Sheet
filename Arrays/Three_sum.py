def three_sum(arr,n):
    result=set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k]==0:
                    result.add(tuple(sorted([arr[i],arr[j],arr[k]])))
    
    final = [list(x) for x in result]
    return final
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The triplets that sum to zero are: ",three_sum(arr,n))

