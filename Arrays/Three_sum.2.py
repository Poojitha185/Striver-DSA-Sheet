#ime Complexity: O(NlogN)+O(N2), as The pointer i, is running for approximately N times. And both the pointers j and k combined can run for approximately N times including the operation of skipping duplicates. So the total time complexity will be O(N2). 

#Space Complexity: O(no. of quadruplets), This space is only used to store the answer. We are not using any extra space to solve this problem. So, from that perspective, space complexity can be written as O(1).

#Two pointers approach is used to solve this problem. We first sort the array and then use  pointers to find the triplets that sum to zero. The first pointer i runs from the start of the array, while the other  pointers j and k run from the next element and the end of the array respectively. We check the sum of the elements at these three pointers and move the pointers accordingly to find all unique triplets that sum to zero.
def three_sum(arr,n):
    arr.sort()
    ans=[]
    for i in range(n):
        if(n>0 and arr[i]==arr[i-1]):
                continue
        j=i+1
        k=n-1
        while(j<k):
            sum=arr[i]+arr[j]+arr[k]
            if sum>0:
                k=k-1
            elif sum<0:
                j=j+1
            else:
                ans.append([arr[i],arr[j],arr[k]])
                j=j+1
                k=k-1
                while(j<k and arr[j]==arr[j-1]):
                    j=j+1
                while(j<k and arr[k]==arr[k+1]):
                    k=k-1
    return ans
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The triplets that sum to zero are: ",three_sum(arr,n))
    