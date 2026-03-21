#TC:O(N) n[::-1] → reverses the string → takes O(N) Comparing n == k → takes O(N)
#SC:O(N) because we are creating a new string k which is the reverse of n
#If we want SC:O(1) we can use two pointers approach or 1 pointer approach to check if the string is a palindrome and not without creating a new string
n=input("enter the string: ")
k=n[::-1]
if n==k:
    print("True")
else:
    print("False")