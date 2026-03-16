n=4
size=2*n-1
for i in range(size):
    for j in range(size):
        min_distance=min(i,j,size-1-i,size-1-j)
        value=n-min_distance
        print(value,end=" ")
    print()