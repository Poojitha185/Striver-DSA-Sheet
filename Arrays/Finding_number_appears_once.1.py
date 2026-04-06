#TC:O(N), as we are iterating through the array once to create the frequency dictionary and then iterating through the frequency dictionary to find the number that appears once.
#SC:O(N), as we are using a dictionary to store the frequency of each element in the array, which can take up to O(N) space in the worst case when all elements are distinct.
#using Dictionary approach
def finding_number_appears_once(arr):
    freq={}             
    for i in arr:          #tc:o(n)
        freq[i]=freq.get(i,0)+1
    for j in freq:         #tc:o(n)
        if freq[j]==1:
         return j
arr=arr=list(map(int,input("enter the arary: ").split(',')))
print("The number that appears once in a array is: ",finding_number_appears_once(arr))