def mergeSorted(nums1 : list[int], m :int, nums2: list[int], n:int):
    """
    Merges two sorted arrays, nums1 and nums2, into a single sorted array in-place.
    
    Args:
    nums1 (list[int]): The first sorted array with additional space for elements from nums2.
    m (int): The number of initial elements in nums1.
    nums2 (list[int]): The second sorted array.
    n (int): The number of elements in nums2.

    Returns:
    None: The function modifies nums1 in-place to contain the merged sorted array.
    """
    last = m+n-1
    while m>0 and n>0:
        if nums1[m-1] > nums2[n-1]:
            nums1[last] = nums1[m-1]
            m-=1
        else:
            nums1[last] = nums2[n-1]
            n-=1
        last -= 1
    while n>0:
        nums1[last] = nums2[n-1]
        n,last = n-1,last-1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

mergeSorted(nums1, m, nums2, n)
print(nums1)