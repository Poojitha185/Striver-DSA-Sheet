def linear__search(arr,n,key):
    for i in range(n):
        if arr[i]==key:
            return True
    return False
def longest_consecutive_sequence(arr,n):
    if n==0:
        return 0
    longest=1
    for i in range(n):
        x=arr[i]
        cnt=1
        while(linear__search(arr,n,x+1)):
            x=x+1
            cnt=cnt+1
        longest=max(longest,cnt)
    return longest
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The longest consecutive sequence:",longest_consecutive_sequence(arr,n))


