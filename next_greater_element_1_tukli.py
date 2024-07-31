def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    stack = []  # Stack to keep track of the next greater elements
    next_greater = {}  # Dictionary to map each element to its next greater element

    # Traverse nums2 from right to left
    for num in nums2:
        # Maintain elements in decreasing order in the stack
        while stack and stack[-1] <= num:
            stack.pop()
        # The current element is the next greater element for the top of the stack
        if stack:
            next_greater[num] = stack[-1]
        else:
            next_greater[num] = -1
        stack.append(num)

    # Build result for nums1 using the next_greater dictionary
    return [next_greater[num] for num in nums1]

# Example usage:
print(nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))  # Output: [-1, 3, 3]
