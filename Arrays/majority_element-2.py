#TC:O(n^2), as we are using nested loops to count the occurrences of each element in the array.
#SC:O(n), as we are using a set to store the unique elements of the array, which in the worst case can be equal to the size of the input array.
def majority_element(arr,n):
  s=set(arr)
  result=[]
  for i in s:
    count=0
    for j in range(n):
      if arr[j]==i:
        count+=1
    if count >(n//3):
       result.append(i)
  return result
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The majority element is: ",majority_element(arr,n))