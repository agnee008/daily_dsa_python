def longestIncreasingSequence(nums: list[int]) -> int:
    """
    Find the length of the longest increasing subsequence in a list of integers.

    Args:
    nums (list[int]): A list of integers.

    Returns:
    int: The length of the longest increasing subsequence.
    
    Example:
    >>> longestIncreasingSequence([10, 9, 2, 5, 3, 7, 101, 18])
    4
    >>> longestIncreasingSequence([0, 1, 0, 3, 2, 3])
    4
    """
    if not nums:
        return 0

    # Create an array `LIS` where `LIS[i]` will be the length of the longest increasing subsequence ending at index `i`
    LIS = [1] * len(nums)

    # Build the LIS array
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                LIS[i] = max(LIS[i], LIS[j] + 1)

    # The length of the longest increasing subsequence is the maximum value in `LIS`
    return max(LIS)

# Example usage
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(f"The length of the longest increasing subsequence is: {longestIncreasingSequence(nums)}")  # Output should be 4




