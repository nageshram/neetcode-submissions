class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        visited=[False]*n
        def backtracking(arr):
            if len(arr)==n:
                res.append(arr.copy())
                return
            

            for i in range(n):
                if not visited[i]:
                    visited[i]=True
                    arr.append(nums[i])
                    backtracking(arr)
                    arr.pop()
                    visited[i]=False

        
        backtracking([])

        return res
            

        