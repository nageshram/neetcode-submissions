class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
        max=1
        for k,v in d.items():
            if v>max:
                max=v
        if max==1:
            return False
        else:
            return True

