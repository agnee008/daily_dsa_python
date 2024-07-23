# O(nlogn)

def makeAllEqual(nums:list[int]):
    nums.sort()
    n = len(nums)
    median = nums[n//2]
    steps = sum(abs(num - median) for num in nums)
    return steps

# Example usage
nums = [1, 2, 3]
print(makeAllEqual(nums))  # Output: 2


# Brute Force (min nums)

def minMoves(nums:list[int]):
    min_value = min(nums)
    max_value = max(nums)
    min_steps =float('inf')

    for target in range(min_value,max_value+1):
        steps = sum(abs(num - target) for num in nums)
        min_steps = min(steps, min_steps)
    return min_steps

# Example usage
nums = [1, 2, 3]
print(minMoves(nums))  # Output: 2