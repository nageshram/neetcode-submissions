class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        #prefix a d suffix max's
        n= len(height)
        suffix =[0]*n
        prefix = [0]*n

        for i in range(n):
            if i==0:
                prefix[i]= height[i]
            else:
                prefix[i]=max(prefix[i-1],height[i])

        for i in range(n-1,-1,-1):
            if i== n-1:
                suffix[i]=height[i]
            else:
                suffix[i]=max(suffix[i+1],height[i])

        for i in range(len(height)):
            res += min(prefix[i],suffix[i])- height[i]
        
        return res if height else 0
