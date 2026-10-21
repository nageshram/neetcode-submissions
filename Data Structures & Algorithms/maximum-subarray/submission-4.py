class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=nums[0]
        current = nums[0]
        for i in range(1,len(nums)):
            current=max(nums[i],current+nums[i])
            maxi=max(maxi,current)
                #inner loop generates more sub arrays 
        return maxi if nums else 0