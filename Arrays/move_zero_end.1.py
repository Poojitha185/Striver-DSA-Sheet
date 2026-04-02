def move_zero_end(arr,n):
     j=-1
     for k in range(n):
          if arr[k]==0:
               j=k
               break
     for i in range(j+1,n):
          if arr[i]!=0:
               arr[j],arr[i]=arr[i],arr[j]
               j=j+1
     return arr
arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
print("array after moving zeros to end: ",move_zero_end(arr,n))
           
          