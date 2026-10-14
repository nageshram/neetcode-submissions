class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=len(nums)*[1]
        suffix =len(nums)*[1]
        l,r=0,len(nums)-1
        res=[]

        while l<len(nums) and r>=0:
            if l==0 and len(nums)-1==r:
                prefix[l]=nums[l]
                suffix[r]=nums[r]
            else:
                prefix[l]=nums[l]*prefix[l-1]
                suffix[r]=nums[r]*suffix[r+1]
            l+=1
            r-=1
        
        for i in range(len(nums)):
            if i==0:
                res.append(suffix[i+1])
            elif i==len(nums)-1:
                res.append(prefix[i-1])
            else:
                res.append(suffix[i+1]*prefix[i-1])
        
        return res

        