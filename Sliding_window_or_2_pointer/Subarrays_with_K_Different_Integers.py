# TC: O(n^2) because we use two nested loops
# SC: O(k) because the frequency dictionary stores at most k distinct elements

#A variable count is initialized with 0. This stores the number of subarrays containing exactly k distinct integers.
#The array is traversed using start as the starting index. For every start, a fresh frequency map is created because a new subarray is being built from that position.
#The end pointer moves from start to the end of the array. Whenever nums[end] is included in the current subarray, its frequency is increased in the map.
#The size of the map tells how many distinct integers are currently present in the subarray. If the map size becomes exactly k, count is increased.
#If the map size becomes greater than k, the loop stops for the current start. This is safe because adding more elements cannot decrease the number of distinct integers. After all starting positions are checked, count is returned.

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