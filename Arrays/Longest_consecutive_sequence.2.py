def longest_consecutive_sequence(arr,n):
    if n==0:
        return 0
    longest=1
    st=set(arr)
    for i in st:
        if i-1  not in st:
            cnt=1
            x=i
            while x+1 in st:
                x=x+1
                cnt=cnt+1
            longest=max(longest,cnt)
    return longest
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The longest consecutive sequence:",longest_consecutive_sequence(arr,n))