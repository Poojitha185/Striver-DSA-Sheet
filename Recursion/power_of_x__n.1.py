#Time Complexity: O(log n), where n is the absolute value of the exponent. This is because we reduce the problem size by half in each recursive call when n is even.

#Space Complexity: O(log n), due to the recursive call stack. In the worst case, the depth of the recursion can go up to log(n) when n is even.



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
                