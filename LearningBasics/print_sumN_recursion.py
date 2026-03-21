#TC:O(N) because we are calling the function N times
#SC:O(N) because of the recursive stack
def sum(N,i,count):
    if i>N:
        return count
    else:
     count=count+i
     return sum(N,i+1,count)
N=int(input("enter the number: "))
print(sum(N,1,0))

