

def repeating_and_missing_numbers(arr,n):
    repeating=0
    missing=0
    for i in range(1,n+1):
        if arr.count(i)>1:
            repeating=i
        elif i not in arr:
            missing=i
    return [repeating, missing]

arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The repeating and missing number in the array is: ",repeating_and_missing_numbers(arr,n))
