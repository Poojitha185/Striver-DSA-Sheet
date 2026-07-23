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
