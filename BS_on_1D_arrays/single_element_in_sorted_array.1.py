#Time Complexity: O(N), N = size of the given array.We are traversing the entire array.

#Space Complexity: O(1) as we are not using any extra space.

#traverse through the array and compare each element with its neighbors, we can detect the unique number. If an element is not equal to its left and right neighbors, then it must be the single number.

def single_element(arr,n):
    if n==0:
      return arr[0]
    for i in range(n):
       if i==0:
          if arr[i]!=arr[i+1]:
             return arr[i]
       elif i==n-1:
           if arr[i]!=arr[i-1]:
              return arr[i]
       else:
          if arr[i]!=arr[i-1] and arr[i]!=arr[i+1]:
             return arr[i]
    return -1
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("the single element in the array is:",single_element(arr,n))