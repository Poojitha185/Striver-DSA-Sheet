def minimum(ind,jumps,arr):
    n=len(arr)
    mini=float('inf')
    if ind>=n-1:
        return jumps
    for i in range(1,arr[ind]+1):
        mini=min(mini,minimum(ind+i,jumps+1,arr))
    return mini

arr=list(map(int,input("Enter the list of maximum jump lengths: ").split(",")))
jumps=0
print(minimum(0,0,arr))