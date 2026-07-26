#Time Complexity: O(2t * k) due to exploring all combinations up to the target with copying each valid combination of average length k.

#Space Complexity: O(k * x) to store all valid combinations, where x is the number of combinations and k is their average length.
#This process is repeated while index < array.size() for a given recursion call.
#A set only removes exactly identical tuples. It doesn't know that (7,1) and (1,7) represent the same combination.Best fixSort the array first
def combination_sum2(ind,target,curr_list,comb_list,arr):
    arr.sort()
    if ind==len(arr):
        if target==0:
            comb_list.add(tuple(curr_list))   #A Python set can only contain hashable/immutable objects. Lists are mutable, so they can't be elements of a set.If you want to use a set, convert the combination to a tuple
        return    
    if arr[ind]<=target:
            curr_list.append(arr[ind])
            combination_sum2(ind+1,target-arr[ind],curr_list,comb_list,arr)
            curr_list.pop()
    combination_sum2(ind+1,target,curr_list,comb_list,arr)

arr=list(map(int,input("enter the array: ").split(',')))
target=int(input("enter the target value: "))
comb_list=set()
combination_sum2(0,target,[],comb_list,arr)
print("The combinations are:")
for i in comb_list:
    print(list(i))

