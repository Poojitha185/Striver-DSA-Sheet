#Time Complexity: O(n), where n is the absolute value of the exponent. This is because we multiply the base x, n times.

#Space Complexity: O(1), as we are using a constant amount of space for the variables used in the computation.

#Initialize the result variable, ans, to 1. This serves as the base case where any number raised to the power of 0 is 1. Check if the exponent n is less than 0: If true, invert x by setting x = 1/x and make n positive by setting n = -n. This transformation allows handling of negative exponents.
#Use a loop to iterate from 0 to n (converted to an integer). In each iteration, multiply ans by x. This effectively computes x raised to the power of n.
#Return the result stored in ans, which now contains the value of x^n.

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

