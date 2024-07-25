def replaceElement(nums: list[int]) -> list[int]:
    # Initialize the maximum element to the right of the last element as -1
    max_element = -1
    # Traverse the list from right to left
    for i in range(len(nums) - 1, -1, -1):
        # Store the current element before modifying it
        current = nums[i]
        # Replace the current element with the maximum element seen so far
        nums[i] = max_element
        # Update the maximum element seen so far
        max_element = max(max_element, current)
    return nums

# Example usage
nums = [17, 18, 5, 4, 6, 1]
print(replaceElement(nums))  # Output: [18, 6, 6, 6, 1, -1]
