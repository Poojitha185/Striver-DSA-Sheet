def find_majority_element(arr,n):
    dic={}
    for i in arr:
        dic[i]=dic.get(i,0)+1
    k=max(dic.values())
    if k>n//2:
        return k,(n+1)//2
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
w,x=find_majority_element(arr,n)
print("The number",w,"appears",x,"times in",n,"sized array")