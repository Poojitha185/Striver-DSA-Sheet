
def longest_odd_string(s,n):
    ind=0
    for i in range(n-1,-1,-1):
        if (int(s[i])%2)==1:
            ind=i
            break
    i=0
    while i<=ind and s[i]=='0':
        i=i+1
    return s[i:ind+1]
s=input("Enter the string: ")
n=len(s)
print("The largest odd number in the string is:",longest_odd_string(s,n))