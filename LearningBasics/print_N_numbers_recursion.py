def printN (N,i=1):
               
    if i>N:
        return 
    else:
      print(i)
    printN(N,i+1)
N=int(input("enter the number: "))
printN(N)

       
    