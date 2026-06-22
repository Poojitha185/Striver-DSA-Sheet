#TC:O(N) where N is the number of characters in the input string, due to the single loop iterating through the words.
#SC:O(N) for the space used to store the list of words and the reversed list.
def reverse(s):
    t=s.split(" ")
    k=[]
    for i in range(len(t)-1,-1,-1):                 #or using builtin function t.reverse()  and return " ".join(t)
        k.append(t[i])
    return " ".join(k)
s=input("enter string:")
print("reversing of string: ",reverse(s))