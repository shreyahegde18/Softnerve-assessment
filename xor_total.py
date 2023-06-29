def subXORSum(nums):
    total = 0

    def backtrack(index, current_xor):
        nonlocal total
        if index == len(nums):
            total += current_xor
            return
        # Include the current element in the subset
        backtrack(index + 1, current_xor ^ nums[index])
        # Exclude the current element from the subset
        backtrack(index + 1, current_xor)

    backtrack(0, 0)
    return total

# Example usage
nums = [5,1,6]
result = subXORSum(nums)
print(result)  # Output: 28

