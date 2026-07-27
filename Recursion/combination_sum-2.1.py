def combination_sum2(ind,target,curr_list,comb_list,arr):
    if target==0:
        comb_list.append(list(curr_list))
        return 
    n=len(arr)
    for i in range(ind,n):
        if i>ind and arr[i]==arr[i-1]:
            continue
        if arr[i]>target:
            break
        curr_list.append(arr[i])
        combination_sum2(i+1,target-arr[i],curr_list,comb_list,arr)
        curr_list.pop()

arr=list(map(int,input("enter the array: ").split(',')))
arr.sort()
target=int(input("enter the target value: "))
comb_list=[]
combination_sum2(0,target,[],comb_list,arr)
print("The combinations are:")
print(comb_list)

