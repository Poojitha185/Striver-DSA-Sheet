#Time Complexity: O(2^N) { This problem involves two function calls for each iteration which further expands to 4 function calls and so on which makes worst-case time complexity to be exponential in nature }.
#Space Complexity: O(N) { At maximum there could be N function calls waiting in the recursion stack since we need to calculate the Nth Fibonacci number for which we also need to calculate (N-1) Fibonacci numbers before it }.
def fib(N):
    if N<=1:
        return N
    else:
         k=fib(N-1)+fib(N-2)
         return k
N=int(input("enter the number: "))
print(fib(N))