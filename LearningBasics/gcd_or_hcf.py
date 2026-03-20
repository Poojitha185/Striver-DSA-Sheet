#using Euclidean algorithm:gcd(a,b)=gcd(a%b,b) if a>b and gcd(a,b)=gcd(a,b%a) if b>a
def gcd(a,b):
    while a>0 and b>0:
        if a>b:
            a=a%b
        else:
            b=b%a
    if a==0:
     print("gcd of a 2 numbers: ",b)
    else:
     print("gcd of a 2 numbers: ",a)
n1=int(input("enter  number1: "))
n2=int(input("enter number2: "))
gcd(n1,n2)