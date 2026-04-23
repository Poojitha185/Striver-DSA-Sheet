def three_sum(arr,n):
    result=set()
    for i in range(n):
        s=set()
        for j in range(i+1,n):
            last=-(arr[i]+arr[j])
            if last in s:
                result.add(tuple(sorted([arr[i],arr[j],last])))
            s.add(arr[j])
    final=[list(x) for x in result]
    return final
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The triplets that sum to zero are: ",three_sum(arr,n))
