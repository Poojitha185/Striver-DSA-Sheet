#TC:O(N*N)
#SC:O(1), as we are not using any extra space 
def number_once(arr):
    for i in arr:               #It also repeats  work(counting) for duplicates and tc:o(n), as we are iterating through the array once.
        if arr.count(i)==1:        #tc:o(n) ,it internally runs a loop to count the number of occurrences of i in the array
         return i
arr=arr=list(map(int,input("enter the arary: ").split(',')))
print("The number that appears once in a array is: ",number_once(arr))
