#Time Complexity: O(N^2), where N is the size of the array. This is because for each element, we are traversing the entire array to count its occurrences.

#Space Complexity: O(1), as we are using a constant amount of space for the result array, which can hold at most 2 elements.

def majority_element(arr,n):
    result=[]
    for i in range(n):
     if len(result)==0 or result[0]!=arr[i]:
        count=0
        for j in range(n):
           if arr[j]==arr[i]:
              count+=1
        if count > n//3:
           result.append(arr[i])
        if len(result)==2:
           break
    return result
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The majority element is: ",majority_element(arr,n))