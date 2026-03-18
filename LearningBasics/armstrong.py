n=input("enter the number: ")
power=len(n)
m=0
for i in n:
    k=int(i)**power
    m=m+k
if int(n)==m:
    print("n is Armstong number")
else:
    print("n is not an Armstrong number")
