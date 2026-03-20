#Backtracking ,initally we will start with the base case and then we will call the function recursively for the next number and then we will print the number after the recursive call so that it will print in descending order
def printN (N,i):
               
    if i>N:
        return 
    else:
     printN(N,i+1)
     print(i)
N=int(input("enter the number: "))
printN(N,1)


       
    