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