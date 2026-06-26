#Time Complexity: O(n), where n is the length of the input string since we traverse the string once.
#Space Complexity: O(1), since we use a fixed-size map for Roman numerals.

def roman_to_integer(s):
    roman = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
    ans=0
    for i in range(len(s)-1):
        if roman[s[i]]<roman[s[i+1]]:
            ans-=roman[s[i]]
        else:
            ans+=roman[s[i]]
    ans+=roman[s[-1]]                  #The final character is always added since there's nothing after it to compare.

    return ans
s=input("Enter the string: ")
print(roman_to_integer(s))
     