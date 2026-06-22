def reverse(s):
    t=s.split(" ")
    k=[]
    for i in range(len(t)-1,-1,-1):
        k.append(t[i])
    return " ".join(k)
s=input("enter string:")
print("reversing of string: ",reverse(s))