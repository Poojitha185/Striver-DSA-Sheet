#Time Complexity: O(2*N), where N is the size of the array. This is because we are iterating through the array once to build the dictionary and then iterating through the dictionary to find the repeating and missing numbers.

#Space Complexity: O(N), as we are using an additional dictionary of size N+1 to store the frequency of each element.

#Dictionary approach: We create a dictionary to count the frequency of each element in the array. Then we iterate through the numbers from 1 to n and check the frequency in the dictionary. If the frequency is 2, it means that number is repeating, and if the frequency is 0, it means that number is missing. Finally, we return the repeating and missing numbers as a list.

def repeating_and_missing_numbers(arr, n):
    k = {}
    repeating = 0
    missing = 0
    for i in arr:
        k[i] = k.get(i, 0) + 1
    for i in range(1, n+1):
        if k.get(i, 0) == 2:
            repeating = i
        elif k.get(i, 0) == 0:
            missing = i

    return [repeating, missing]


arr = list(map(int, input("enter the array: ").split(',')))
n = len(arr)
print("The repeating and missing number in the array is:", repeating_and_missing_numbers(arr, n))