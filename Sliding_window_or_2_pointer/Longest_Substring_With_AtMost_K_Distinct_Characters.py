
#Time Complexity: O(N²), where N represents the string length. Expansion from every starting position may process many later characters.

#Space Complexity: O(N), because the frequency map may store many distinct characters for a general string.

class Solution:

    # Expands from every start
    # while tracking frequencies.
    def longest_substring_at_most_k_distinct(
        self,
        s: str,
        k: int
    ) -> int:
        n = len(s)

        # No valid non-empty substring
        # can exist in these cases.
        if n == 0 or k <= 0:
            return 0

        max_length = 0

        # Try every possible start.
        for start in range(n):
            frequency = {}

            # Grow the current substring.
            for end in range(start, n):
                current = s[end]

                frequency[current] = (
                    frequency.get(current, 0) + 1
                )

                # Further expansion cannot
                # reduce the distinct count.
                if len(frequency) > k:
                    break

                max_length = max(
                    max_length,
                    end - start + 1
                )

        return max_length


if __name__ == "__main__":
    s = "eceba"
    k = 2

    solution = Solution()

    print(
        solution.longest_substring_at_most_k_distinct(
            s,
            k
        )
    )