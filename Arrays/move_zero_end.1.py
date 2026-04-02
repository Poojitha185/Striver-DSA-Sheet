#TC:O(N), as we are iterating through the array once to find the first zero and then iterating through the remaining elements to move non-zero elements to the left.
#SC:O(1) bcz we are not using extra space for creating new array and modifying original array in place
#using two pointer approach
def move_zero_end(arr,n):
     j=-1
     for k in range(n):    #tc:O(k) where k is the index of first zero in the array
          if arr[k]==0:
               j=k
               break
     for i in range(j+1,n): #tc=O(N-k) where n is the size of the array and k is the index of first zero in the array
          if arr[i]!=0:
               arr[j],arr[i]=arr[i],arr[j]
               j=j+1
     return arr
arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
print("array after moving zeros to end: ",move_zero_end(arr,n))
           
          