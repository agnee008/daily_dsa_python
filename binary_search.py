def binarySearch(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        middle = (left + right) // 2
        value_middle = nums[middle]

        if value_middle == target:
            return middle
        elif value_middle < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1 
