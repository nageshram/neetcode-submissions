class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)
        dp = [[-1]*(n+1) for _ in range(m+1)]
        def solve(i, j):
            if i==0:
                return j
            if j==0:
                return i
            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i-1] == word2[j-1]:
                dp[i][j]=solve(i-1, j-1)
            else:
                insert = 1+ solve(i,j-1)
                delete = 1+ solve(i-1, j)
                replace = 1+ solve(i-1, j-1)
                dp[i][j]= min(insert, delete, replace)
            return dp[i][j]

        return solve(m,n)

