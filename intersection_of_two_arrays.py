def intersection(nums1:list[int], nums2:list[int]):
    hashmap_1 = set()
    hashmap_2 = set()

    for i in nums1:
        if i not in hashmap_1:
            hashmap_1.add(i)

    for j in nums2:
        if j not in hashmap_2:
            hashmap_2.add(j)
    return list(hashmap_1.intersection(hashmap_2))
    
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print(intersection(nums1, nums2))  # Output: {2}