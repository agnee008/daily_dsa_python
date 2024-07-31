def convertToZigzag(nums:list[int]):
    nums.sort()
    for i in range(1, len(nums) -1, 2):
        nums[i], nums[i+1] = nums[i+1], nums[i]
    print(nums)

convertToZigzag([4, 3, 7, 8, 6, 2, 1])