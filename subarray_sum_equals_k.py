def subarraySumEqualsK(nums:list[int], k:int):
    curSum = 0
    prefixSum = {0:1}

    res = 0

    for n in nums:
        curSum += n
        diff = curSum - k
        res += prefixSum.get(diff,0)
        prefixSum[curSum] = 1 + prefixSum.get(curSum,0)
        
    return res

print(subarraySumEqualsK([-2,-3,4,-1,-2,1,5,-3], 7))