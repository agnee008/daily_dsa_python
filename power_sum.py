def powerSum(nums:list[list[int]], pow = 1):
    """
    Calculate the sum of numbers in a nested list, raising each element to the specified power.

    Args:
    nums (list): A nested list of integers.
    pow (int): The power to which each element should be raised (default is 1).

    Returns:
    int: The sum of all elements in the list, each raised to the specified power.
    """
    sum = 0 

    for i in nums:
        if isinstance(i,list):
            sum += powerSum(i, pow)
        else:
            sum += pow**i
    return sum
