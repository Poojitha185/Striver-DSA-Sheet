def two_sum(arr,n,target):
   seen={}
   for i,num in enumerate(arr):
      com=target-num
      if com in seen:
         return "YES",[seen[com],i]
      seen[num]=i
   return "NO",[-1,1]
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
target=int(input("enter the target sum: "))

status, indices = two_sum(arr, n, target)

print(status)
if status == "YES":
    print("The numbers present in indices:", indices)
else:    
    print("No such pair of numbers found in the array.")