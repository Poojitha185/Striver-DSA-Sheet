#Time Complexity: O(2n * k), For each of the 2n subsequences, storing takes O(k) time where k is the average length of each combination.

#Space Complexity: O(k * x), To store all x valid combinations, each of average length k.

#Sort the array before starting recursion to ensure combinations are in sorted order and to avoid duplicates.
#Begin recursion from index 0 and explore each element for inclusion in the current combination.
#If the current element is suitable (≤ target), add it to the combination and move to the next index.
#Skip over duplicate elements to avoid generating the same combination again.
#After the recursive call, backtrack by removing the last added element from the combination.
#Terminate early if the current element exceeds the target, as further elements (being sorted) will only be larger.

def combination_sum2(ind,target,curr_list,comb_list,arr):
    if target==0:
        comb_list.append(list(curr_list))
        return 
    n=len(arr)
    for i in range(ind,n):
        if i>ind and arr[i]==arr[i-1]:    #i>ind is wrote bcz same elements containing combination can be skipped bcz of arr[i]==arr[i-1] condition this condition ensures that if same elements picking again at same position then only it can be that combionation to avoid duplicates.#
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
print(comb_list)                       #print lists of list

