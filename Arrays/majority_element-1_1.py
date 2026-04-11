def majority_element(arr,n):
    for i in range(n):
        count=0
        for j in range(n):
            if arr[i]==arr[j]:
             count +=1
        if count>n//2:
           return arr[i],count
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
w,x=majority_element(arr,n)
print("The number",w,"appears",x,"times in",n,"sized array")
        