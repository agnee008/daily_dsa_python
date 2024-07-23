def missingNumber(nums: list[int]):
    list_sum = sum(nums)
    n = len(nums) + 1  # Because we need to include the missing number in the range
    arithmetic_sum = n * (n + 1) // 2  # Sum of first n natural numbers (0 to n-1)
    missing_number = arithmetic_sum - list_sum
    return missing_number

print(missingNumber([1, 2, 3, 5, 6]))  # Output should be 4



def missingAllNumber(nums: list[int]):
    complete_set = set(range(min(nums), max(nums) + 1))
    nums_set = set(nums)
    missing_numbers = list(complete_set - nums_set)
    missing_numbers.sort()
    return missing_numbers

print(missingAllNumber([1, 2, 5, 6]))  # Output should be 4



