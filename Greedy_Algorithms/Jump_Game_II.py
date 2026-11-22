#Time Complexity: Exponential — \(O(2^n)\) upper bound
   #- At every index, you can make multiple recursive calls.
   #- Each call explores all possible jump lengths.
   #- The same index can be visited through different paths, so subproblems are repeated.
#A tighter general bound for this recursion is \(O(2^n)\).
#Space Complexity: \(O(n)\)
   #- Recursion stack stores function calls.
   #- In the worst case, recursion can go up to n levels (when jumping one position at a time).

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