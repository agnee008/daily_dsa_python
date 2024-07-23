def powerSet(nums: list[int]) -> list[list[int]]:
    """
    Generate the power set of a given list of integers.

    Args:
        nums (list[int]): The list of integers to generate the power set for.

    Returns:
        list[list[int]]: A list containing all subsets of the input list.

    Raises:
        ValueError: If the input list is empty.

    Example:
        >>> powerSet([1, 2, 3])
        [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    """
    output= []

    if not nums:
        raise ValueError("Input cannot be blank")
    
    def helper(nums,i,subset):
        if i == len(nums):
            output.append(subset.copy())
            return
        subset.append(nums[i])
        helper(nums,i+1,subset)
        subset.pop()
        helper(nums,i+1,subset)


    helper(nums,0,[])
    return output

if __name__=="__main__":
    nums= [1,3,4]
    print(powerSet(nums))

