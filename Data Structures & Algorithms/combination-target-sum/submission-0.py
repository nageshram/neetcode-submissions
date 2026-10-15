class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res =[]

        def backtrack(start, path, total):

            if total == target:
                res.append(path.copy())
                return

            if start >= len(nums) or total > target:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, path, total+nums[i])
                path.pop()
            
            # we can also implement backtracking in this way  here start is renamed to ' i'
            #path.append(nums[i])
            #backtrack(i, path, total+nums[i]) # including current number once 
            #path.pop() 
            #backtrack(i+1, path, total) # excluding current number once 
        
        backtrack(0,[],0)

        return res

