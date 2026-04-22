def majority_element(arr,n):
    dic={}
    result=[]
    for i in range(n):
        dic[arr[i]]=dic.get(arr[i],0)+1
    for i,j in dic.items():
        if j>n//3:
            result.append(i)
        if len(result)==2:
            break
    return result
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The majority element is: ",majority_element(arr,n))