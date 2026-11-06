# TC: O(n^2) because we use two nested loops
# SC: O(k) because the frequency dictionary stores at most k distinct elements

def longest_substring_at_most_k_distinct(arr,k):
        count=0
        for start in range(len(arr)):
            frequency = {}
            for end in range(start, len(arr)):
                frequency[arr[end]] = (frequency.get(arr[end], 0) + 1)
                if len(frequency)==k:
                    count+=1
                if len(frequency) > k:
                    break
        return count

arr=list(map(int,input("enter the array: ").split(",")))
k=int(input("Enter the value of k: "))
print(longest_substring_at_most_k_distinct(arr,k))