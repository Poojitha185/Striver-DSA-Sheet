#TC:O(n*logn) at worst case
#SC:O(n) at worst case
#uses dictionary method
def sort_chars_by_frequency(s):
    k={}
    l=[]
    for i in s:
        k[i]=k.get(i,0)+1
    #uses the key parameter of sorted() to specify how the items should be sorted.A lambda is a small anonymous function.
    result = sorted(k.items(), key=lambda x: (-x[1], x[0]))  #-x[1] Makes the frequency sort in descending order.
                                                             # x[0] If two characters have the same frequency, sort them alphabetically
    for key,item in result:
        l.append(key)
    return l
s=input("enter the string: ")
print("the sorted string based on frequency of characters is: ",sort_chars_by_frequency(s))