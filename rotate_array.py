def rotateArray(nums: list[int], k: int) -> list[int]:
    """
    Rotate the array to the right by k steps.

    Args:
        nums (list[int]): The list of integers to be rotated.
        k (int): The number of steps to rotate the array.

    Returns:
        list[int]: The array after rotating it to the right by k steps.

    Example:
        >>> rotateArray([1, 4, 5, 6, 7], 3)
        [5, 6, 7, 1, 4]

    Notes:
        - The function first calculates the effective number of steps `k` by taking `k % len(nums)`.
        - It then extracts the last `k` elements into `temp`.
        - It shifts the first part of the array (excluding the last `k` elements) to the right by `k` positions.
        - Finally, it places the elements from `temp` at the beginning of the array.
    """
    k = k % len(nums)  # Ensure k is within the bounds of the array length

    temp = nums[-k:]  # Extract the last k elements

    # Shift the elements in the original array to the right to make space for temp
    for i in reversed(range(len(nums) - k)):
        nums[i + k] = nums[i]
    
    # Place the extracted elements at the beginning of the array
    for i in range(len(temp)):
        nums[i] = temp[i]
    
    return nums



def rotateArray_m2(nums: list[int], k: int) -> list[int]:
    """
    Rotate the array to the right by k steps using the reversal algorithm.

    Args:
        nums (list[int]): The list of integers to be rotated.
        k (int): The number of steps to rotate the array.

    Returns:
        list[int]: The array after rotating it to the right by k steps.

    Example:
        >>> rotateArray_m2([1, 4, 5, 6, 7], 3)
        [5, 6, 7, 1, 4]

    Notes:
        - The function first calculates the effective number of steps `k` by taking `k % len(nums)`.
        - It then reverses the entire array.
        - After that, it reverses the first `k` elements.
        - Finally, it reverses the remaining elements to complete the rotation.
    """
    k = k % len(nums)  # Ensure k is within the bounds of the array length

    def reverse(nums: list[int], start: int, end: int):
        """
        Reverse a portion of the array from index start to end.

        Args:
            nums (list[int]): The list of integers to be reversed.
            start (int): The starting index of the portion to reverse.
            end (int): The ending index of the portion to reverse.

        Returns:
            None: The list is modified in place.
        """
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Reverse the entire array
    reverse(nums, 0, len(nums) - 1)
    # Reverse the first k elements
    reverse(nums, 0, k - 1)
    # Reverse the remaining elements
    reverse(nums, k, len(nums) - 1)

    return nums
