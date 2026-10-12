#Time Complexity: O(N³), where N represents the array size. O(N²) continuous sections exist, and validation of one section may scan up to N elements.
#Space Complexity: O(1), because the validation set stores at most three fruit types before detecting an invalid section. The basket limit remains fixed at two.

#A valid collection can begin and end at any pair of tree positions. Therefore, every possible continuous section must receive examination.
#For each selected section, a fresh set records distinct fruit types. A section remains valid when the set contains at most two types. Complete checking guarantees the correct answer, but repeated scanning of overlapping sections creates considerable extra work.
class Solution:

    # Finds the longest valid section by checking every possible range.
    def total_fruit(self, fruits: list[int]) -> int:
        n = len(fruits)
        max_fruits = 0

        # Try every tree as the beginning of a collection.
        for start in range(n):

            # Try every possible ending position for the current start.
            for end in range(start, n):
                types = set()

                # Count distinct fruit types inside the selected range.
                for i in range(start, end + 1):
                    types.add(fruits[i])

                    # More than two types makes this range invalid.
                    if len(types) > 2:
                        break

                # Longer ranges from this start will also remain invalid.
                if len(types) > 2:
                    break

                max_fruits = max(
                    max_fruits,
                    end - start + 1
                )

        return max_fruits
if __name__ == "__main__":
    fruits = [1, 2, 1, 2, 3]

    solution = Solution()

    print(solution.total_fruit(fruits))