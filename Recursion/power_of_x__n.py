def myPow(x, n):
        if n == 0 or x == 1.0:
            return 1
        temp = n  # to avoid integer overflow
        # Handle negative exponents
        if n < 0:
            x = 1 / x
            temp = -1 * n
        ans = 1
        for i in range(temp):
            # Multiply ans by x for n times
            ans *= x 
        return float(ans)
x=float(input("Enter the value of x: "))
n=int(input("Enter the value of n: "))
print(myPow(x, n))

