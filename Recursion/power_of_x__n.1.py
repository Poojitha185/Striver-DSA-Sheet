#Time Complexity: O(log n), where n is the absolute value of the exponent. This is because we reduce the problem size by half in each recursive call when n is even.

#Space Complexity: O(log n), due to the recursive call stack. In the worst case, the depth of the recursion can go up to log(n) when n is even.

#If the exponent n is even: If true, recursively calculate the power by squaring the base and halving the exponent:
#power(x, n) = power(x * x, n / 2)
#If the exponent n is odd: If true, recursively calculate the power by multiplying the base with the result of the power function for n - 1:
#power(x, n) = x * power(x, n - 1)
#Handle negative exponents:
#If the exponent is negative, calculate the power for the positive exponent and take the reciprocal of the result.

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
                