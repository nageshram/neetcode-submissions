class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n=len(s)
        if not s or n <= 0:
            return 0
        if n==1:
            return 1
        
        l, r=0,1
        maxi=0
        sub=s[0]
        
        while l < n and r < n:
            if s[r] in sub:
                while s[r] in s[l:r]:
                    l+=1
                r+=1
            else:
                r+=1
            sub = s[l:r]
            maxi = max(maxi, len(s[l:r]))
        
        return maxi




