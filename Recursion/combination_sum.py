#Time Complexity: O(2t * k) due to exploring all combinations up to the target with copying each valid combination of average length k.

#Space Complexity: O(k * x) to store all valid combinations, where x is the number of combinations and k is their average length.

#questions like printing combinations or subsequences, the first thing that should strike your mind is recursion.
#At every step, we have two choices:
    #Pick the element at the current index:
    #We reduce the target by arr[index].
    #Add arr[index] to the DS.
    #We stay on the same index since we can reuse the same element.
#Not pick the element:
    #We move to the next index.
    #Target remains unchanged.
    #Element is not added to the DS.
#While backtracking, remove the last inserted element to explore new paths.
#This process is repeated while index < array.size() for a given recursion call.

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

