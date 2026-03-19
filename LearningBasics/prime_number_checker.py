n=int(input("enter the number:"))
j=0
for i in range(2,n):
    if n%i==0:
       j=j+1
if j>0:
    print(n,"is nota prime number")
else:
    print(n,"is a prime number")