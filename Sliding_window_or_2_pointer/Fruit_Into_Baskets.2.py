#Time Complexity: O(N), where N represents the array size. The right pointer processes every fruit once, while the left pointer moves only forward.
#Space Complexity: O(N) in the worst case for the single-if variant. Temporary invalid windows may retain more than two fruit types inside the frequency map. A standard while-based shrink keeps the map bounded by the basket limit and uses O(1) auxiliary space for two baskets.

#Starting a fresh expansion from every index repeats earlier work. A sliding window keeps one active section and allows both boundaries to move only forward.
#The right pointer adds fruits to the section. After a third type appears, a single left-side fruit is removed during the same iteration. A single if condition may leave the window temporarily invalid, but an invalid window never grows beyond the best valid length because one fruit enters and one fruit leaves together. The answer changes only after the window contains at most two fruit types again.

def total_fruit(fruits):
        frequency = {}
        left = 0
        max_fruits = 0
        right=0
        while(right<len(fruits)):  #o(n) for travelling entire array.
            fruit = fruits[right]
            frequency[fruit] = (frequency.get(fruit, 0) + 1)
            if len(frequency) > 2:
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