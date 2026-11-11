class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        l, r = 0, len(heights)-1
        while l<r:
            w= abs(l-r)
            hei = min(heights[l],heights[r])
            maximum = max(maximum, w*hei)
            if heights[r] >= heights[l]:
                l+=1
            else:
                r-=1
        
        return maximum

