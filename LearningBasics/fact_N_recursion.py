#using recursion
#TC:O(N) because we are calling the function N times
#SC:O(N) because of the recursive stack
def fact(N):
    if (N==0):
        return 1
    else:
        return N*fact(N-1)
N=int(input("enter the number: "))
print(fact(N))