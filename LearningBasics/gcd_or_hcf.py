#using Euclidean algorithm:gcd(a,b)=gcd(a%b,b) if a>b and gcd(a,b)=gcd(a,b%a) if b>a 
#TC:O(log(min(a,b))) as we are reducing the problem size by a factor of 2 in each step and S.C:O(1) as we are not using any extra space
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