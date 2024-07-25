from typing import List

def maxProductSubarray(nums:List[int]):
    max_product = float('-inf')

    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums)):
            product *= nums[j]
            max_product = max(product, max_product)
    return max_product


nums = [2, 3, -2, 4]
print(maxProductSubarray(nums))  # Output: 6