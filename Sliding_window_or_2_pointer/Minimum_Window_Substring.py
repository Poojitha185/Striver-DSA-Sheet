#Time Complexity (TC) :O(n² × m × n) = O(n³ × m), n² – Two nested loops generate all possible substrings. m – Loop through every character in t. n – count() takes O(n) time in the worst case.
#Space Complexity (SC):O(n + m), O(n) – Creating the current window substring. O(m) – Storing the input string t (if counting input space).

def minimum_window_substring(s,t):
    mincount=float('inf')
    substring=''
    for i in range(len(s)):
        for j in range(i,len(s)):
         for k in t:
            if k not in s[i:j+1] or s[i:j+1].count(k) < t.count(k):
             break
         else:
            if mincount>j-i+1:
              substring=(s[i:j+1])
              mincount=j-i+1
    return substring
s=input("Enter the string s: ")
t=input("Enter the string t: ")
result=minimum_window_substring(s,t)
print("The minimum window substring is:",result)
            


