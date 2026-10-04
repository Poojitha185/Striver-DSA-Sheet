class Solution:

    # Uses last-seen positions
    # to move the left boundary directly.
    def length_of_longest_substring(
        self,
        s: str
    ) -> int:
        last_seen = {}

        left = 0
        max_len = 0

        # Move right across the string.
        for right in range(len(s)):
            current = s[right]

            # Move left only when the
            # duplicate is inside the window.
            if (
                current in last_seen
                and last_seen[current] >= left
            ):
                left = last_seen[current] + 1

            last_seen[current] = right

            max_len = max(
                max_len,
                right - left + 1
            )

        return max_len


if __name__ == "__main__":
    s = "abcabcbb"

    solution = Solution()

    print(solution.length_of_longest_substring(s))