def combination_sum(ind,target,curr_list,comb_list,arr):
    if ind==len(arr):
        if target==0:
            comb_list.append(list(curr_list))
        return 
    if arr[ind]<=target:
            curr_list.append(arr[ind])
            combination_sum(ind,target-arr[ind],curr_list,comb_list,arr)
            curr_list.pop()
    combination_sum(ind+1,target,curr_list,comb_list,arr)

arr=list(map(int,input("enter the array: ").split(',')))
target=int(input("enter the target value: "))
comb_list=[]
combination_sum(0,target,[],comb_list,arr)
print("The combinations are:")
for i in comb_list:
    print(i)

