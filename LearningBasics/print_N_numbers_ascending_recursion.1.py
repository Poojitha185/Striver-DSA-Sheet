#Backtracking ,initally we will start with the base case and then we will call the function recursively for the next number and then we will print the number after the recursive call so that it will print in ascending order
#Work happens AFTER recursive call → Backtracking and Explore all possibilities(USED IN Permutations,combinations,subsets etc)
#TC:O(N) as we are calling the function N times and 
# SC:O(N) as we are using the stack space for N function calls
def printN (N,i):
               
    if i<1:
        return 
    else:
     printN(N,i-1)
     print(i)
N=int(input("enter the number: "))
printN(N,N)


       
    