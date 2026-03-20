#This is optimal approach to find divisors of a number as we are only iterating till sqrt(n) and not n
# TC:O(sqrt(n)) S.C:O(n) as we are storing the factors in a list and in worst case we can have n factors for a number

n=int(input("enter the number to find divisors: "))
k=[]
for i in range(1,int(n**0.5)+1):
    if n%i==0:
       k.append(i)           #first factor
       if ((n//i)!=i):
           k.append(n//i)      #second factor
k.sort()                         #T.c=o(nlogn) as we are sorting the list of factors
print(k)
