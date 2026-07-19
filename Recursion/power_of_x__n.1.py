def power(x,n):
    if n == 0:
            return 1.0
    if n==1:
          return x
    if n%2==0:
          return power(x*x,n//2)
    if n%2!=0:
          return x*power(x,n-1)
def sign_n(x,n):
      if n<0:
            return 1/power(x,-n)
      return power(x,n)
x=float(input("enter the x value: ") )
n=int(input("enter the n value: "))
print(sign_n(x,n))     
                