def candies(ratings: list[int]):
    # Initiate an array with all 1 as each one will have at least one candy

    nums = [1] * len(ratings)

    # Left to right
    for i in range(1, len(ratings)):
        if ratings[i-1] < ratings[i]:
            nums[i] = nums[i-1] + 1

    # Right to left
    for i in range(len(nums) -2, -1, -1):
        if ratings[i] > ratings[i+1]:
            nums[i] = max(nums[i],nums[i+1] + 1)

    return sum(nums)


print(candies([1,0,2]))