def moveZeroes(nums:list[int]):
    l = 0  # noqa: E741

    for r in range(len(nums)):
        if nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1  # noqa: E741

    return nums

print(moveZeroes([1,0,6,7,0,3,4,2]))