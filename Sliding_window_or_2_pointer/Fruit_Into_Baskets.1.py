# TC: O(2n) - Each fruit is added and removed from the window at most once.
# SC: O(1) - Frequency dictionary stores at most 3 fruit types temporarily.

#we keep on moving left till subarray become valid again using while loop which overall takes o(n) time so total time complexity o(n)+o(n)=o(2n)

def total_fruit(fruits):
        frequency = {}
        left = 0
        max_fruits = 0
        right=0
        while(right<len(fruits)):  #o(n) for travelling entire array.
            fruit = fruits[right]
            frequency[fruit] = (frequency.get(fruit, 0) + 1)
            if len(frequency) > 2:
                while(len(frequency) > 2):    #o(n) for travelling entire array at worst case.
                  left_fruit = fruits[left]
                  frequency[left_fruit] -= 1
                # Remove a type after its final fruit leaves the window.
                  if frequency[left_fruit] == 0:
                    del frequency[left_fruit]
                left += 1
            if len(frequency) <= 2:
                max_fruits = max(max_fruits,right - left + 1)
            right += 1
        return max_fruits

fruits=list(map(int, input("Enter the array of fruits: ").split(",")))
result=total_fruit(fruits)
print("Maximum number of fruits that can be collected:", result)