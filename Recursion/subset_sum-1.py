#Time Complexity: O(2n),Each element has two choices: include or exclude, leading to 2n subsets. We directly compute sums without iterating over subsets, so complexity is O(2n). Sorting the sums adds O(2n log(2n)), making the total O(2n log(2n)).

#Space Complexity: O(2n),The result array holds all subset sums, requiring O(2n) space. Recursion uses an additional O(n) stack space due to function calls, so total auxiliary space is O(2n + n).
#Initialize an empty list to store sums
#Create a recursive function taking index and current sum as parameters If index equals N, push the current sum into the list and return
#Recursively call the function including the current element (sum + arr[index])
#Recursively call the function excluding the current element (sum remains the same)
#We can solve this more cleanly using recursion without generating all bitmasks. Start from index 0, maintain a running sum, and at each index, make two recursive calls—one including the current element and one excluding it. When we reach the end of the array, store the current sum in our result list. This avoids explicitly storing subsets, reduces unnecessary operations, and still generates all sums in O(2^N) time. Sorting at the end gives the required increasing order.
def subset_sum(ind,sum,arr,ans):
    n=len(arr)
    if ind==n:
        ans.append(sum)
        return 
    subset_sum(ind+1,sum+arr[ind],arr,ans)
    subset_sum(ind+1,sum,arr,ans)
def find(arr,ans):
    subset_sum(0,0,arr,ans)
    ans.sort()
    return ans
arr=list(map(int,input("enter the array: ").split(',')))
ans=[]
print(find(arr,ans))



