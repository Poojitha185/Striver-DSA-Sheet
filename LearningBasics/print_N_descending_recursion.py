def printN (N,i):
               
    if i<1:
        return 
    else:
     print(i)
     printN(N,i-1)
N=int(input("enter the number: "))
printN(N,N)


       
    