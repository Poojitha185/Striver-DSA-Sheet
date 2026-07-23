#Time Complexity: O(2^n) (Catalan number): C(n) = (2n)! / (n!(n+1)!) is the number of valid sequences.Each sequence takes O(n) to build.So, total complexity: O(C(n) × n)

#Space Complexity: O(n) recursion depth. O(C(n) × n) to store results.

#Start with an empty string curr = "".
#Initialize counters: open = 0, close = 0.
#If open < n, add '(' and recurse.
#If close < open, add ')' and recurse.
#If curr.length == 2 * n, add it to the result.


def backtrack(curr, open, close, n, res):
    if len(curr) == 2 * n:
        res.append(curr)
        return
    if open < n:
        backtrack(curr + '(', open + 1, close, n, res)
    if close < open:
        backtrack(curr + ')', open, close + 1, n, res)

def generate_parenthesis(n):
    res = []
    backtrack("", 0, 0, n, res)
    return res

n=int(input("enter the n value: "))
print("The generated parenthesis are:")
res=generate_parenthesis(n)
for i in res:
    print(i)
