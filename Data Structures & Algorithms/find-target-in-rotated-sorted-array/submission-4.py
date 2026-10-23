class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n= len(nums)
        def binsearch(start,end):
            while start<=end:
                mid=((start+end)//2)
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    start = mid+1
                else:
                    end= mid-1
            return -1
            

        l1, r1 = 0,nums.index(max(nums))
        l2, r2 = r1+1,n-1
        res1 = binsearch(l1,r1)
        if res1 != -1:
            return res1
        
        res2 = binsearch(l2, r2)
        return res2


            
            
