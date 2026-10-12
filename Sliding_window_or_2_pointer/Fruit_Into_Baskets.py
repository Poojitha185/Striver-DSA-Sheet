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