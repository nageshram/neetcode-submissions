class Solution:
    def hammingWeight(self, n: int) -> int:
        if n<=0:
            return 0
        count = 0
        while n:
            r=n%2
            if r==1:
                count+=1
            n=n//2
            
        return count
        
