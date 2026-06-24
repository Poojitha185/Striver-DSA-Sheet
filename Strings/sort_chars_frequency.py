#Time Complexity: O(n + k log k), where n is the length of the string and k is the constant 26 for the alphabet.

#Space Complexity: O(k) , where k is the constant 26 for the frequency array.

#We need a structure that can track both the character and how often it occurs.

#Sorting the characters by frequency helps surface the most significant ones first.

#To maintain consistency when frequencies match, tie-breaking is done alphabetically.

def sort_chars_by_frequency(s):
    k={}
    l=[]
    for i in s:
        k[i]=k.get(i,0)+1
    #uses the key parameter of sorted() to specify how the items should be sorted.A lambda is a small anonymous function.
    result = sorted(k.items(), key=lambda x: (-x[1], x[0]))  #-x[1] Makes the frequency sort in descending order.
                                                             # x[0] If two characters have the same frequency, sort them alphabetically
    for key,item in result:
        if item>0:
         l.append(key)
    return l
s=input("enter the string: ")
print("the sorted string based on frequency of characters is: ",sort_chars_by_frequency(s))