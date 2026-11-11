class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = float('-inf')

        seen = set(nums)

        for i in range(len(nums)):
            #if num-1 is exist it is already the part of some sequnce so if 
            # num -1 is not exist then that is the start of continuos sequnce 
            if nums[i]-1 in seen:
                continue
            else:
                current = 0
                num=nums[i]
                while num in seen:
                    current+=1
                    num+=1
                longest = max(current, longest)

        return longest if longest != float('-inf') else 0
        