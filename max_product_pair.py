def maxProductPair(nums:list[int]):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num


        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    product1 = max1 * max2
    product2 = min1 * min2

    if product1> product2:
        return (max1,max2)
    else:
        return (min1, min2)


# Example usage
arr1 = [1, 4, 3, 6, 7, 0]
arr2 = [-1, -3, -4, 2, 0, -5]

print(maxProductPair(arr1))  # Output: (6, 7)
print(maxProductPair(arr2))  # Output: (-4, -5)