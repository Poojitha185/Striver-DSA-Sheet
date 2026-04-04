def intersection(arr1,arr2,n1,n2):
       ans=[]
       i=0
       j=0
       while(i<n1 and j<n2):
            if arr1[i]<arr2[j]:
                     i=i+1
            elif(arr2[j]<arr1[i]):
                    j=j+1
            else:
                ans.append(arr2[j])
                i=i+1
                j=j+1  
       return ans
arr1=list(map(int,input("enter the first sorted arary: ").split(',')))
arr2=list(map(int,input("enter the second sorted arary: ").split(',')))
n1=len(arr1)
n2=len(arr2)
print("intersection of two sorted arrays: ",intersection(arr1,arr2,n1,n2))
              
              
              