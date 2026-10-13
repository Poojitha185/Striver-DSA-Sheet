#Time Complexity: O(N³), where N represents the array size. O(N²) continuous sections exist, and validation of one section may scan up to N elements.
#Space Complexity: O(1), because the validation set stores at most three fruit types before detecting an invalid section. The basket limit remains fixed at two.

# Approach:
#A valid collection can begin and end at any pair of tree positions. Therefore, every possible continuous section must receive examination.
#For each selected section, a fresh set records distinct fruit types. A section remains valid when the set contains at most two types. Complete checking guarantees the correct answer, but repeated scanning of overlapping sections creates considerable extra work.

def total_fruit(fruits,n):
        max_fruits = 0
        # Try every tree as the beginning of a collection.
        for start in range(n):
            # Try every possible ending position for the current start.
            types = set()
            for end in range(start, n):
                types.add(fruits[end])
                    # More than two types makes this range invalid.
                if len(types) <=2:
                     max_fruits = max(max_fruits,end - start + 1)
                else:
                    break          
        return max_fruits
fruits=list(map(int, input("Enter the array of fruits: ").split(",")))
n = len(fruits)
result=total_fruit(fruits,n)
print("Maximum number of fruits that can be collected:", result)