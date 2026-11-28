class Solution:
    def jump(self, nums: List[int]) -> int:
        n= len(nums)
        dp={}
        def dfs(i):

            if i == n-1:
                return 0
            
            if i in dp:
                return dp[i]
            if nums[i]==0:
                return 1000000

            end = min(n, i+nums[i]+1)
            res = 1000000
            for j in range(i+1,end):
                res = min(res, 1+dfs(j))

            dp[i]=res

            return res

        return dfs(0)
