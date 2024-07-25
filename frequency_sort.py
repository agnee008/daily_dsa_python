from collections import Counter
def frequencySort(nums:list[int]):
    count = Counter(nums)

    def custom_sort(n):
        return(count[n], -n)
    nums.sort(key=custom_sort)
    return nums