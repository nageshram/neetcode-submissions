class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or  s[0] == '0':
            return 0

        dp = [0] * len(s)
        dp[0] = 1

        for i in range(1,len(s)):
            num = int(s[i-1:i+1])

            if s[i] != '0':
                dp[i] += dp[i-1] 

            if num <= 26 and num >= 10:
                dp[i] += dp[i-2] if i>=2 else 1
            
        return dp[-1]

        
        