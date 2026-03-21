#TC:O(N) because we are traversing the array once
#SC:O(N) because we are using an extra array to store the reversed array
#bbrute force approach
def reverse(n,k):
    rev=[]
    for i in range(n-1,-1,-1):
        rev.append(k[i])
    return rev
n=int(input("enter the number of elements: "))
k=[]
print("enter the array elements: ")
for j in range(n):
    k.append(int(input()))
print(reverse(n,k))

        