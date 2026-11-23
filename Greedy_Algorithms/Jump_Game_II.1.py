def minimum(jumps):
    n=len(jumps)
    jump=0
    l,r=0,0
    while r<n-1:
        farthest=0
        for i in range(l,r+1):
            farthest=max(farthest,i+jumps[i])
        l=r+1
        r=farthest
        jump+=1
    return jump
jumps=list(map(int,input("Enter the list of maximum jump lengths: ").split(",")))
print(minimum(jumps))


