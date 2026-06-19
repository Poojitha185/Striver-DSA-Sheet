def largest_common_prefix(strs,n):
    first=strs[0]
    last=strs[-1]
    ans=[]
    for i in range(min(len(first),len(last))):
        if first[i]!=last[i]:
            return ''.join(ans)
        ans.append(first[i])
    return ''.join(ans)
strs = eval(input("Enter list of strings: "))
n=len(strs)
print("The longest common prefix is:", largest_common_prefix(strs,n))
