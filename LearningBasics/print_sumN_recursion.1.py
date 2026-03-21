# using formula n(n+1)/2
#TC:O(1) because we are using a formula to calculate the sum
#SC:O(1) because we are using a constant space to store the sum
def sum(N):
    return (N*(N+1))//2
N=int(input("enter the number: "))
print(sum(N))