def permutations(nums: list[int]) -> list[list[int]]:
    """
    Generate all permutations of a given list of integers.

    Args:
        nums (list[int]): The list of integers to generate permutations for.

    Returns:
        list[list[int]]: A list containing all permutations of the input list.

    Raises:
        ValueError: If the input list is empty.

    Example:
        >>> permutations([1, 2, 3])
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
    """
    perm = []

    if len(nums) == 0:
        raise ValueError("Cannot accept empty input")
    
    def helper(nums, i):
        if i == len(nums) - 1:
            perm.append(nums.copy())
            return
        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            helper(nums, i + 1)
            nums[i], nums[j] = nums[j], nums[i]
    
    helper(nums, 0)
    return perm

if __name__ == "__main__":
    nums = [1, 2, 5, 6, 7]
    print(permutations(nums))
