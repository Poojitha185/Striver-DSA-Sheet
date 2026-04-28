#TC:O(N^2), as we are iterating through the array once to check for each number from 1 to n if it is repeating or missing, and the count() method itself takes O(N) time.
#SC:O(1), as we are not using any extra space to store the frequency of elements or any other data structure, we are just using two variables to store the repeating and missing numbers.
def repeating_and_missing_numbers(arr,n):
    repeating=0
    missing=0
    for i in range(1,n+1):
        if arr.count(i)>1:    #tc:O(n) 
            repeating=i
        elif i not in arr:    #tc:O(n)
            missing=i
    return [repeating, missing]

arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The repeating and missing number in the array is: ",repeating_and_missing_numbers(arr,n))
