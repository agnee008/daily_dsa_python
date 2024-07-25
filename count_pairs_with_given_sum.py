def countPairs(nums:list[int], k:int):
    pair_count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == k:
                pair_count += 1
    return pair_count


print(countPairs([1, 5, 7, -1], 6))
