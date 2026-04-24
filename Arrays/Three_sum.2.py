def three_sum(arr,n):
    arr.sort()
    ans=[]
    for i in range(n):
        if(n>0 and arr[i]==arr[i-1]):
                continue
        j=i+1
        k=n-1
        while(j<k):
            sum=arr[i]+arr[j]+arr[k]
            if sum>0:
                k=k-1
            elif sum<0:
                j=j+1
            else:
                ans.append([arr[i],arr[j],arr[k]])
                j=j+1
                k=k-1
                while(j<k and arr[j]==arr[j-1]):
                    j=j+1
                while(j<k and arr[k]==arr[k+1]):
                    k=k-1
    return ans
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The triplets that sum to zero are: ",three_sum(arr,n))
    