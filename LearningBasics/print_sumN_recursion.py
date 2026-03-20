def sum(N,i,count):
    if i>N:
        return count
    else:
     count=count+i
     return sum(N,i+1,count)
N=int(input("enter the number: "))
k=sum(N,1,0)
print(k)
