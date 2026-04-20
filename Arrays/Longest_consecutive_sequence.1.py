def longest_consecutive_sequence(arr,n):
    if n==0:
        return 0
    arr.sort()
    cnt=1
    longest=1
    lastsmaller=arr[0]
    for i in range(n):
        if(arr[i]-1==lastsmaller):
            cnt=cnt+1
            lastsmaller=arr[i]
        elif(arr[i]-1!=lastsmaller):
            cnt=1
            lastsmaller=arr[i]
        longest=max(longest,cnt)
    return longest
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The longest consecutive sequence:",longest_consecutive_sequence(arr,n))