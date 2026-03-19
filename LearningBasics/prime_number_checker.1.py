n=int(input("enter the number to find divisors: "))
count=0
for i in range(1,int(n**0.5)+1):
    if n%i==0:
       count=count+1       #first factor
       if ((n//i)!=i):
           count=count+1     #second factor
if count==2:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")