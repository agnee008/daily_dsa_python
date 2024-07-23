# Twp Sum

def two_sum_m1(nums:list[int], target:int):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []
