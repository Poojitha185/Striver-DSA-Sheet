#Time Complexity: O(2^(2n) * n) due to the generation and validation of all 2^(2n) sequences.

#Space Complexity: O(n) space required per sequence.

#Generate all sequences of length 2n.
#For each sequence, use a validator to check conditions.
#Ensure the count of ')' never exceeds '(' at any point.
#At the end of the sequence, the count must be 0.
def is_valid(s):
    balance=0
    for c in s:
        if c=='(':
            balance+=1
        elif c==')':
            balance-=1
        if balance<0:
            return False
    return balance==0
def generate_all(curr,n,result):
    if len(curr) == 2*n:
        if is_valid(curr):
            result.append(curr)
        return
    generate_all(curr + '(', n, result)  #Both choices are explored, but one after the other. Recursion doesn't execute them simultaneously.
    generate_all(curr + ')', n, result)
def generate_parenthesis(n):
    result=[]
    generate_all("",n,result)
    return result
n=int(input("enter the n value: "))
print("The generated parenthesis are:")
res=generate_parenthesis(n)
for i in res:
    print(i)