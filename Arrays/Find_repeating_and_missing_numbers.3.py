#Time Complexity: O(N), where N is the size of the array. This is because we are iterating through the array to calculate the XOR values.

#Space Complexity: O(1), as we are using a constant amount of space for variables, regardless of the input size.

class Solution:
    # Function to find repeating and missing numbers
    def findMissingRepeatingNumbers(self, nums):
        
        # size of the array
        n = len(nums)

        xr = 0

        for i in range(n):
            # XOR of all elements in nums
            xr = xr ^ nums[i] 
            
            # XOR of numbers from 1 to n
            xr = xr ^ (i + 1)  

        # Get the rightmost set bit in xr
        number = (xr & ~(xr - 1))

        # Group the numbers based on the differentiating bit
        # Number that falls into the 0 group
        zero = 0 
        
        # Number that falls into the 1 group
        one = 0  

        for i in range(n):
            """ Check if nums[i] belongs to the 1 group
             based on the differentiating bit"""
            if (nums[i] & number) != 0:
                
                # XOR operation to find numbers in the 1 group
                one = one ^ nums[i]
                
            else:
                # XOR operation to find numbers in the 0 group
                zero = zero ^ nums[i]

        # Group numbers from 1 to n based on differentiating bit
        for i in range(1, n + 1):
            
            # Check if i belongs to the 1 group 
            # based on the differentiating bit
            if (i & number) != 0:
                # XOR operation to find numbers in the 1 group
                one = one ^ i
                
            else:
                # XOR operation to find numbers in the 0 group
                zero = zero ^ i

        # Count occurrences of zero in nums
        cnt = 0

        for i in range(n):
            if nums[i] == zero:
                cnt += 1

        if cnt == 2:
            """ zero is the repeating number,
             one is the missing number"""
            return [zero, one]

        """ one is the repeating number, 
        zero is the missing number"""
        return [one, zero]

if __name__ == "__main__":
    nums = [3, 1, 2, 5, 4, 6, 7, 5]
    
    # Create an instance of Solution class
    sol = Solution()

    result = sol.findMissingRepeatingNumbers(nums)

    # Print the repeating and missing numbers found
    print(f"The repeating and missing numbers are: {{{result[0]}, {result[1]}}}")
