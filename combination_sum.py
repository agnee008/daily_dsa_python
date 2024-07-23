def combinationSum(candidates:list[int], target:int):
    output = []

    def helper(i,curr,total):
        if target == total:
            output.append(curr.copy())
            return
        if i>=len(candidates) or total > target:
            return
        curr.append(candidates[i])
        helper(i,curr,total+candidates[i])
        curr.pop()
        helper(i+1,curr,total)
    
    helper(0,[],0)
    return output

candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))