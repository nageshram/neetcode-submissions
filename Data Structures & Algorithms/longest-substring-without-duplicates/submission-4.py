class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        seen=set()
        maxi=0

        for  r in range(len(s)):
            #remove chars until if dont fin dthe duplicates 
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            maxi = max(maxi, r-l+1)
        return maxi