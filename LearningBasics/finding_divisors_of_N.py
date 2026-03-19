n=int(input("enter the number to find divisors: "))
k=[]
for i in range(1,n+1):
    if n%i==0:
       k.append(i)
print(k)