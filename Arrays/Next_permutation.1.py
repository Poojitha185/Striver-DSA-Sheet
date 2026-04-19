#Time Complexity: O(N), we find the breaking point and reverse the subarray in linear time.
#Space Complexity: O(1), constant additional space is used.

def next_permutation(num,n):
   index=-1
   for i in range(n-2,-1,-1):
      if num[i]<num[i+1]:
         index=i
         break
   if index==-1:
      num.reverse()
      return
   for i in range(n-1,index,-1):
         if num[i]>num[index]:
             num[i],num[index]=num[index],num[i]
             break
   num[index+1:]=reversed(num[index+1:])
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
next_permutation(arr,n)
print("the next permutation is: ",arr)